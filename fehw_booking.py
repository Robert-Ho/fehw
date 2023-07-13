from page_objects import Page,HomePage,Result, Book_secure_page
from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
import datetime
import re
import pytest
import random

class Booking_Steps():
    def open_home_page(self,sb):
        sb.maximize_window()
        if sb.env=='uat':
            sb.open("https://fareasthospitalityuat.feodigitallab.com.sg/")
        elif sb.env == 'production':
            sb.open('https://www.fareasthospitality.com/')
        else: 
            sb.open('https://fareasthospitalitydev.feodigitallab.com.sg/')

    def close_popup(self,sb):
        # sb.open_home_page()
        if sb.is_element_visible(HomePage.close_dialog):
            sb.click(HomePage.close_dialog)
            sb.sleep(2)

    def open_booking_wedget(self,sb):   
        if not sb.is_element_visible(HomePage.booking_wg):
            sb.click(HomePage.booknow_bt)

    def select_hotel_by_booknow(self,sb,locationName,hotelsName):
        sb.click(HomePage.drop_down_location1)
        sb.assert_element(f"//*[@id='header-booknow-widget']/div[1]/div[1]/div/div/ul//a/span[contains(text(),'{locationName}')]",f"Cannot find location{locationName}")
        sb.click(f"//*[@id='header-booknow-widget']/div[1]/div[1]/div/div/ul//a/span[contains(text(),'{locationName}')]")
        sb.assert_element(f"//*[@id='header-booknow-widget']/div[1]/div[2]/div/div/ul//a/span[contains(text(),'{hotelsName}')]")
        sb.click(f"//*[@id='header-booknow-widget']/div[1]/div[2]/div/div/ul//a/span[contains(text(),'{hotelsName}')]")
        
    def select_hotel_by_default(self, sb, locationName, hotelsName):
        sb.click(HomePage.drop_down_location2)
        sb.click(f"//form[@id='BookingWidgetForm']//li//span[contains(text(),'{locationName}')]")
        sb.click(f"//form[@id='BookingWidgetForm']//li//a/span[contains(text(),'{hotelsName}')]")
        
    def select_checkIn_checkOut(self, sb, checkIn= None, checkOut= None):    
        # if checkOut-checkIn < self.get_first_number()
        
        if checkIn == None and checkOut == None:
            return
        if not sb.is_element_visible('div#ui-datepicker-div'):
            if sb.is_element_visible("input#checkin2"):
                sb.click("input#checkin2")
            else: sb.click('input#widget-checkin')
                            #table.ui-datepicker-calendar td[data-month='6'][data-year='2023'] a[data-date='15']
        self.move_to_correct_month(sb,checkIn)
        # checkIn_locator  = f"table.ui-datepicker-calendar td[data-month='{checkIn.month-1}'][data-year='{checkIn.year}'] a[data-date='{checkIn.day}']"
        # checkOut_locator = f"table.ui-datepicker-calendar td[data-month='{checkOut.month-1}'][data-year='{checkOut.year}'] a[data-date='{checkOut.day}']"
        # if not sb.is_element_visible(checkIn_locator):
        #     sb.click(checkIn_locator)
        if checkIn != None:
            self.pick_aDay(sb,checkIn)
        sb.sleep(2)
        if checkOut != None:
            self.pick_aDay(sb,checkOut)

    def pick_aDay(self,sb,checkIn):
        if not sb.is_element_visible('div#ui-datepicker-div'):
            if sb.is_element_visible("input#checkin2"):
                sb.click("input#checkin2")
            else: sb.click('input#widget-checkin')
        checkIn_locator  = f"table.ui-datepicker-calendar td[data-month='{checkIn.month-1}'][data-year='{checkIn.year}'] a[data-date='{checkIn.day}']"
        sb.click(checkIn_locator)

    
    def date_is_clickable(self,sb,date):
        check_date  = f"table.ui-datepicker-calendar td[data-month='{date.month-1}'][data-year='{date.year}'] a[data-date='{date.day}']"
        print(sb.is_element_clickable(check_date))
        return sb.is_element_clickable(check_date)
    def move_to_correct_month(self, sb, selc_date):
        month_names = {
            'January': 1,
            'February': 2,
            'March': 3,
            'April': 4,
            'May': 5,
            'June': 6,
            'July': 7,
            'August': 8,
            'September': 9,
            'October': 10,
            'November': 11,
            'December': 12
        }
        actual_mon_name = sb.get_text(HomePage.datepicker_mon)
        actual_mon = int(month_names[actual_mon_name])
        actual_year = int(sb.get_text(HomePage.datepicker_yar))
        print(actual_mon, actual_year,selc_date.month, selc_date.year)
     
        if selc_date.year == actual_year and selc_date.month == actual_mon:
            return
        else:
            while selc_date.year != actual_year:
                print (f"năm đã chọn {selc_date.year} <> actual year {actual_year}")
                if selc_date.year > actual_year:
                    sb.click(HomePage.datepicker_next_mon)
                else: sb.click(HomePage.datepicker_prev_mon)
                actual_year = int(sb.get_text(HomePage.datepicker_yar))
            
            while selc_date.month != actual_mon:
                print (f"thang da chon {selc_date.month} và tháng hiển thị {actual_mon}")
                if selc_date.month > actual_mon:
                    sb.click(HomePage.datepicker_next_mon)
                else: sb.click(HomePage.datepicker_prev_mon)
                actual_mon_name = sb.get_text(HomePage.datepicker_mon)
                actual_mon = int(month_names[actual_mon_name])

    def number_of_guest(self, sb, adutl, child):
        if adutl < 1:
            print("a")

    def get_first_number(self,sb, locator):
        string = sb.get_text(locator)
        numbers = re.findall(r'\d+', string)

        if numbers:
            number = int(numbers[0])
            print("Number:", number)
            return number
        else:
            print("No number found in the string.")
            return None
    def perform_promo_code(self, sb,code):
        if not code==None:
            sb.scroll_to(HomePage.check_availability_bt1)
            sb.click_link_text("Promo/IATA Code")
            sb.type(HomePage.text_box_promocode1,code)
    def perform_promo_code_default(self, sb,code):
        print(code)
        if not code==None:
            sb.scroll_to(HomePage.check_availability_bt2)
            sb.click_link_text("Promo/IATA Code")
            sb.type(HomePage.text_box_promocode2,code)

    def submit_by_booknow(self,sb):
        sb.click(HomePage.check_availability_bt1)

    def submit_default(self,sb):
        sb.click(HomePage.check_availability_bt2)


    def find_hotels_by_booknow(self,sb,location, hotelName, checkIn,checkOut,adult = 2, child= 0,promocode = None):
        self.select_hotel_by_booknow(sb,location, hotelName)
        self.select_checkIn_checkOut(sb,checkIn, checkOut)
        self.perform_promo_code(sb, promocode)
        self.submit_by_booknow(sb)
    
    def find_hotels_by_default(self,sb,location, hotelName, checkIn,checkOut,adult = 2, child= 0, promocode = None):
        print(adult, child, promocode)
        self.select_hotel_by_default(sb,location, hotelName)
        self.select_checkIn_checkOut(sb,checkIn, checkOut)
        self.perform_promo_code_default(sb,promocode)
        self.submit_default(sb)
        # bo sung chon guest sau

class Result_Steps():
    def get_hotel_details(self, sb):
        print(sb.get_domain_url(sb.get_current_url()))
        if sb.get_domain_url(sb.get_current_url()) == "https://www.book-secure.com":
            sb.click(Book_secure_page.smenu_hotel_details)
            return sb.get_text(Book_secure_page.hotel_details_title)
        else:
            sb.click(Result.menu_hotel_info)
            sb.click(Result.smenu_hotel_details)
            return sb.get_text(Result.hotel_details_des)
    
    
        

class Test_Booking(BaseCase):
    def test_booking_with_CTA_BookNow(self):
        Booking_Steps().open_home_page(self)
        Booking_Steps().close_popup(self)
        Booking_Steps().open_booking_wedget(self)
        self.assert_element(HomePage.booking_wg)
        checkIn = datetime.date.today()
        checkOut = datetime.date.today() + datetime.timedelta(days=2)
        Booking_Steps().find_hotels_by_booknow(self,"Singapore, Singapore","Oasia Hotel Downtown",checkIn, checkOut)
        # self.assert_title("Oasia Hotel Downtown by Far East Hospitality - Reservations - Room Availability")
        self.assert_text("OASIA HOTEL DOWNTOWN BY FAR EAST HOSPITALITY", Result.hotel_name)

    def test_booking_with_promoCode(self):
        #give
        location= "Singapore, Singapore"
        hotel_name = "Oasia Residence, Singapore"
        checkIn = datetime.date.today()
        checkOut = datetime.date.today() + datetime.timedelta(days=8)
        pro_code = '123456'
        # adults = 4
        # children = 0
        # #expected
        # title_ex = "Oasia Residence Singapore by Far East Hospitality - Reservations - Room Availability"
        # hotel_name_ex = "OASIA RESIDENCE SINGAPORE BY FAR EAST HOSPITALITY"

        Booking_Steps().open_home_page(self)
        Booking_Steps().close_popup(self)
        Booking_Steps().find_hotels_by_default(self, location, hotel_name,checkIn, checkOut, None,None,pro_code)
        self.assert_text(pro_code,Result.promo_textbox)

    def test_early_checkIn_date(self):
        #give
        location= "Singapore, Singapore"
        hotel_name = "Oasia Hotel Downtown"
        checkOut = datetime.date.today() - datetime.timedelta(days=8)
        

        Booking_Steps().open_home_page(self)
        Booking_Steps().close_popup(self)
        Booking_Steps().select_hotel_by_default(self,location,hotel_name)
        Booking_Steps().move_to_correct_month(self,checkOut)
        self.assert_false(Booking_Steps().date_is_clickable(self,checkOut),f"\nTo day is[{datetime.date.today()}] \nThe check-in date [{checkOut}] should be in a disabled state (grayed out) - not clickable instead of being clickable")
    
    def test_early_checkOut(self):
        #give
        location= "Singapore, Singapore"
        hotel_name = "Oasia Hotel Downtown"
        checkIn = datetime.date.today()
        checkOut = datetime.date.today() - datetime.timedelta(days=8)
        

        Booking_Steps().open_home_page(self)
        Booking_Steps().close_popup(self)
        Booking_Steps().select_hotel_by_default(self,location,hotel_name)
        Booking_Steps().select_checkIn_checkOut(self,checkIn)
        Booking_Steps().move_to_correct_month(self,checkOut)
        self.assert_false(Booking_Steps().date_is_clickable(self,checkOut),f"The check-Out date [{checkOut}] should be in a disabled state (grayed out) - not clickable instead of being clickable")

    def test_booking_withOut_location(self):
        location= "Singapore, Singapore"
        hotel_name = "Oasia Hotel Downtown"
        checkIn = datetime.date.today()
        checkOut = datetime.date.today() + datetime.timedelta(days=8)
        adults = 4
        children = 0
        #expected
        title_ex = "Oasia Residence Singapore by Far East Hospitality - Reservations - Room Availability"
        hotel_name_ex = "OASIA HOTEL DOWNTOWN BY FAR EAST HOSPITALITY"

        Booking_Steps().open_home_page(self)
        Booking_Steps().close_popup(self)
        self.click(HomePage.drop_down_hotels_2)
        self.click(f"//form[@id='BookingWidgetForm']//li//a/span[contains(text(),'{hotel_name}')]")
        Booking_Steps().submit_default(self)
        self.assert_text(hotel_name_ex, Result.hotel_name)

    def test_booking_reselect_location(self):
        #give
        location1   = "Queensland, Australia"
        hotel_name1 = "Oasia Hotel Novena"
        location2   = "Singapore, Singapore"
        hotel_name2 = "Oasia Residence, Singapore"
        checkIn = datetime.date.today()
        checkOut = datetime.date.today() + datetime.timedelta(days=8)
        adults = 4
        children = 0
        #expected
        title_ex = "Oasia Residence Singapore by Far East Hospitality - Reservations - Room Availability"
        hotel_name_ex = "OASIA RESIDENCE SINGAPORE BY FAR EAST HOSPITALITY"

        Booking_Steps().open_home_page(self)
        Booking_Steps().close_popup(self)
        Booking_Steps().select_hotel_by_default(self,location1,hotel_name1)
        self.sleep(2)
        Booking_Steps().select_hotel_by_default(self,location2,hotel_name2)
        Booking_Steps().submit_default(self)
        self.assert_text(hotel_name_ex, Result.hotel_name)

    def test_booking_empty_data(self):
        err_mes = "Please select Property, Check-in Date & Check-out Date"
        Booking_Steps().open_home_page(self)
        Booking_Steps().close_popup(self)
        
        Booking_Steps().submit_default(self)
        self.assert_text(err_mes, HomePage.err_mes2)

    def test_booking_random_singapore(self):
        #give
        location= "Singapore, Singapore"
        Singapore= {
                    "Rendezvous Hotel Singapore": "RENDEZVOUS HOTEL SINGAPORE BY FAR EAST HOSPITALITY",
                    "Village Hotel Sentosa":"VILLAGE HOTEL SENTOSA BY FAR EAST HOSPITALITY",
                    "The Barracks Hotel Sentosa":"THE BARRACKS HOTEL SENTOSA BY FAR EAST HOSPITALITY",
                    "Orchard Parksuites": "ORCHARD PARKSUITES BY FAR EAST HOSPITALITY",
                    "Adina Serviced Apartments Singapore Orchard" :"ADINA SERVICED APARTMENTS SINGAPORE ORCHARD",
                    }
        hotel_name, hotel_name_ex = random.choice(list(Singapore.items()))
        print("Hotel name:", hotel_name)
        print("Hotel title expected:", hotel_name_ex)
        checkIn = datetime.date.today()
        checkOut = datetime.date.today() + datetime.timedelta(days=8)
        adults = 4
        children = 0
        #expected

        Booking_Steps().open_home_page(self)
        Booking_Steps().close_popup(self)
        Booking_Steps().open_booking_wedget(self)
        self.assert_element(HomePage.booking_wg)
        
        Booking_Steps().find_hotels_by_booknow(self,location,hotel_name,checkIn, checkOut,adults, children)

        actual_checkIn = datetime.datetime.strptime(self.get_text(Result.checkIn_date), "%a, %d %b %Y").date()
        actual_checkOut = datetime.datetime.strptime(self.get_text(Result.checkOut_date), "%a, %d %b %Y").date()
        self.assert_true(checkIn == actual_checkIn)
        self.assert_true(checkOut == actual_checkOut)
        self.assert_text(hotel_name_ex, Result.hotel_name)

    def test_booking_random_perth_australia(self):
        #give
        location= "Perth, Australia"
        hotels= {
                    "Vibe Hotel Subiaco Perth" : "Vibe Hotel Subiaco Perth",
                    "Rendezvous Hotel Perth Scarborough" : "Rendezvous Hotel Perth Scarborough"
                    }
        hotel_name, hotel_name_ex = random.choice(list(hotels.items()))
        print("Hotel name:", hotel_name)
        print("Hotel title expected:", hotel_name_ex)
        checkIn = datetime.date.today()
        checkOut = datetime.date.today() + datetime.timedelta(days=8)
        adults = 4
        children = 0
        #expected

        Booking_Steps().open_home_page(self)
        Booking_Steps().close_popup(self)
        Booking_Steps().open_booking_wedget(self)
        self.assert_element(HomePage.booking_wg)
        
        Booking_Steps().find_hotels_by_booknow(self,location,hotel_name,checkIn, checkOut,adults, children)
        if hotel_name == "Vibe Hotel Subiaco Perth":
            self.assert_text(hotel_name_ex, "//div[@class = 'user-bar_hotelName']")
        else:
            des = Result_Steps().get_hotel_details(self)
            print(self.get_domain_url(self.get_current_url()))
            self.assertTrue(hotel_name in des)
            

    def test_booking_random_jakarta_indonesia(self):
        #give
        location= "Jakarta, Indonesia"
        hotels= {   
                "ARTOTEL Thamrin - Jakarta"             :"ARTOTEL Thamrin Jakarta" ,
                "ARTOTEL Suites Mangkuluhur Jakarta"    :"ARTOTEL Suites Mangkuluhur Jakarta"
                }
        hotel_name, hotel_name_ex = random.choice(list(hotels.items()))
        print("Hotel name:", hotel_name)
        print("Hotel title expected:", hotel_name_ex)
        checkIn = datetime.date.today()
        checkOut = datetime.date.today() + datetime.timedelta(days=8)
        adults = 4
        children = 0
        #expected

        Booking_Steps().open_home_page(self)
        Booking_Steps().close_popup(self)
        Booking_Steps().open_booking_wedget(self)
        self.assert_element(HomePage.booking_wg)
        
        Booking_Steps().find_hotels_by_booknow(self,location,hotel_name,checkIn, checkOut,adults, children)
        des = Result_Steps().get_hotel_details(self)
        print
        self.assertTrue(hotel_name_ex in des)
            