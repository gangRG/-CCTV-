import requests
import xml.etree.ElementTree as ET
from datetime import datetime

class TrafficAccidentAPI:
    def __init__(self):
        self.api_key = ""
        self.base_url = "https://opendata.koroad.or.kr/api/rest"
        
    def get_accident_data(self, sido_code="11", gugun_code="", year="2023"):
        """서울 전체 사고다발지역 데이터 조회"""
        all_accidents = []
        page = 1
        max_pages = 20
        
        print(f"서울시 사고다발지역 데이터 조회 시작 ({year}년)")
        
        while page <= max_pages:
            url = f"{self.base_url}/AccidentMultiSpot"
            params = {
                'authKey': self.api_key,
                'searchYearCd': year,
                'siDo': sido_code,
                'guGun': gugun_code,
                'type': 'xml',
                'numOfRows': 100,
                'pageNo': page
            }
            
            try:
                print(f"페이지 {page} 조회 중...")
                response = requests.get(url, params=params, timeout=15)
                
                if response.status_code != 200:
                    print(f"HTTP 오류: {response.status_code}")
                    print(f"응답 내용: {response.text[:200]}")
                    break
                
                root = ET.fromstring(response.content)
                result_code = root.findtext('.//resultCode', '')
                result_msg = root.findtext('.//resultMsg', '')
                total_count = int(root.findtext('.//totalCount', '0'))
                
                print(f"API 응답 - 코드: {result_code}, 메시지: {result_msg}, 총 건수: {total_count}")
                
                if result_code == '00':  # 성공
                    page_accidents = self._parse_xml_response(root)
                    
                    if not page_accidents:
                        print(f"페이지 {page}에서 데이터 없음, 조회 종료")
                        break
                    
                    all_accidents.extend(page_accidents)
                    print(f"페이지 {page}: {len(page_accidents)}건 수집, 총 {len(all_accidents)}/{total_count}건")
                    
                    if len(all_accidents) >= total_count:
                        print("모든 데이터 수집 완료")
                        break
                        
                elif result_code == '03':
                    print("데이터 없음")
                    break
                else:
                    print(f"API 오류: {result_code} - {result_msg}")
                    break
                    
            except Exception as e:
                print(f"페이지 {page} 조회 실패: {e}")
                break
            
            page += 1
        
        print(f"최종 수집된 서울시 사고지점: {len(all_accidents)}개")
        return all_accidents  # 샘플 데이터 제거, 빈 리스트라도 그대로 반환
    
    def _parse_xml_response(self, root):
        """XML에서 사고 데이터 파싱"""
        accidents = []
        
        for item in root.findall('.//item'):
            try:
                lat_str = item.findtext('la_crd', '')
                lon_str = item.findtext('lo_crd', '')
                spot_name = item.findtext('spot_nm', '')
                
                if not lat_str or not lon_str or not spot_name:
                    continue
                
                accident = {
                    'id': item.findtext('afos_id', f'accident_{len(accidents)}'),
                    'spot_name': spot_name,
                    'address': item.findtext('sido_sgg_nm', ''),
                    'lat': float(lat_str),
                    'lon': float(lon_str),
                    'accident_count': int(item.findtext('occrrnc_cnt', '0')),
                    'death_count': int(item.findtext('dth_dnv_cnt', '0')),
                    'injury_count': int(item.findtext('caslt_cnt', '0')),
                    'severe_injury': int(item.findtext('se_dnv_cnt', '0')),
                    'light_injury': int(item.findtext('sl_dnv_cnt', '0'))
                }
                
                # 심각도 계산
                if accident['death_count'] > 0:
                    accident['severity'] = '사망'
                elif accident['severe_injury'] > 0:
                    accident['severity'] = '중상'
                else:
                    accident['severity'] = '경상'
                    
                accidents.append(accident)
                
            except (ValueError, TypeError) as e:
                print(f"데이터 파싱 오류: {e}")
                continue
                
        return accidents