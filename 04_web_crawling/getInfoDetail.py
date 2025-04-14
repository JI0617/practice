
def getInfoDetail(driver, seoul_gu):

    seoul_oil_station=[]
    gu_list=[] # 구 
    car_wash_list=[] # 세차장
    charging_list=[] #충전소
    maintenance_list=[] #경정비
    convenience_list=[] #편의점
    sel24_list=[] #24시 영업
    self_list=[] #셀프 
    name_list = [] #주유소 명
    brand_list=[] #브랜드
    address_list=[] #주소
    gasolin_price_list=[] # 가솔린가격
    diesel_price_list=[] #경유가격

    car_wash='' 
    charging='' 
    maintenance='' 
    convenience='' 
    sel24='' 
    self='' 

    req=driver.page_source
    soup=BeautifulSoup(req,'html.parser')        
    result_oil_info=soup.select_one('.result_gis #os_price1 #body1')
    time.sleep(2) 

    # 해당 구의 모든 주유소: 주유소명, 브랜드, 주소 
    oil_detail_list=result_oil_info.select('.rlist')

    #구 리스트
    gu_list=[seoul_gu for i in range(len(oil_detail_list)) ]


    for idx, detail in tqdm(enumerate(oil_detail_list)):

        # 셀프 여부 
        if '셀프' in detail.text.strip():
            self='Y'
        else:
            self='N'

        self_list.append(self)

        # inner info 
        #Beautiful Soup을 이용하여 주유소 데이터 추출
        # 로딩되기 전 데이터를 불러올 경우 에러 발생 

        rlist=driver.find_element(By.CSS_SELECTOR,f'#body1 > tr:nth-child({idx+1}) > td.rlist > a')

        time.sleep(4) 

        # 각 주유소를 클릭해서 inner info 접근 
        rlist.click()
        time.sleep(4) 

        req=driver.page_source
        soup=BeautifulSoup(req,'html.parser')
        inner_station_info=soup.select_one('.ollehmap-info #os_dtail_info')

        name = inner_station_info.select_one('#os_nm').text #주유소 명
        brand=inner_station_info.select_one('#poll_div_nm').text #브랜드
        address=inner_station_info.select_one('#rd_addr').text #주소
        gasolin_price=inner_station_info.select_one('#b027_p').text # 가솔린가격
        diesel_price=inner_station_info.select_one('#d047_p').text #경유가격


        # 각 리스트에 추가 
        name_list.append(name)
        brand_list.append(brand)
        address_list.append(address)
        gasolin_price_list.append(gasolin_price)
        diesel_price_list.append(diesel_price)


        # 부가정보 데이터 
        # 세차장, 충전소, 경정비, 편의점, 24시 영업
        service_info=inner_station_info.select_one('.service')
        #세차장 
        car_wash_img=service_info.select_one('#cwsh_yn').get('src')
        if 'off' in car_wash_img:
            car_wash='N'
        else:
            car_wash='Y'

        # 충전소
        charging_img=service_info.select_one('#lpg_yn').get('src')
        if 'off' in charging_img:
            charging='N'
        else:
            charging='Y'
        # 경정비
        maintenance_img=service_info.select_one('#maint_yn').get('src')
        if 'off' in maintenance_img:
            maintenance='N'
        else:
            maintenance='Y'
        #편의점
        convenience_img=service_info.select_one('#cvs_yn').get('src')
        if 'off' in convenience_img:
            convenience='N'
        else:
            convenience='Y'
        # 24시 영업
        sel24_img=service_info.select_one('#sel24_yn').get('src')
        if 'off' in convenience_img:
            sel24='N'
        else:
            sel24='Y'

        # 각 리스트에 추가  
        car_wash_list.append(car_wash)
        charging_list.append(charging)
        maintenance_list.append(maintenance)
        convenience_list.append(convenience)
        sel24_list.append(sel24)

        time.sleep(2)


    # 주유소 데이터 통합 
    data={
        '주유소명' : name_list,
        '주소' : address_list,
        '브랜드' : brand_list,
        '휘발유 가격' : gasolin_price_list,
        '경유 가격' : diesel_price_list,
        '셀프 여부' : self_list,
        '세차장 여부' : car_wash_list,
        '충전소 여부' : charging_list,
        '경정비 여부' : maintenance_list,
        '편의점 여부' : convenience_list,
        '24시간 운영 여부' : sel24_list,
        '구' : gu_list
    }

    print(data)


    return data 
