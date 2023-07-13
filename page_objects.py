# PAGE OBJECTS FILE >>> (autogenerated)


class Page(object):
    html = "html"
    
    css_2 = "//nav[@class='navbar navbar-default']//div[@class='desktop-only']//a[@id='top-book-now']"
    css_3 = "div.desktop-only > div >div.grey-bg:nth-child(1)"
    css_4 = "select#location"
    css_5 = "select#property"
    css_6 = "div.desktop-only > div >div.grey-bg button.check-availability-btn"

class HomePage(object):
    close_dialog = "//div[@class='modal-dialog']//div[@class=' modal-inner ']/button"
    booknow_bt = "//nav[@class='navbar navbar-default']//div[@class='desktop-only']//a[@id='top-book-now']"
    booking_wg = "div.desktop-only > div"

    # location_select = "select#location"
    # property_select = "select#property"
    # locations = 'div.desktop-only > div >div.grey-bg div.location'

    drop_down_location1 = "div.desktop-only > div >div.grey-bg:nth-child(1) button[data-id='location']"
    check_availability_bt1 = "div.desktop-only > div >div.grey-bg button.check-availability-btn"
    text_box_promocode1 = 'div.desktop-only input#promocode'

    drop_down_location2 = "//form[@id='BookingWidgetForm']//button[@data-id='location']"
    drop_down_hotels_2 = "//form[@id='BookingWidgetForm']//button[@data-id='property1']"
    check_availability_bt2 = "//form[@id='BookingWidgetForm']//button[@type='submit']"
    text_box_promocode2 = 'div.SFE_banner_booking_widget  input#promocode'
    err_mes2            = "//form[@id='BookingWidgetForm']//div[@class='error-placement']"
    datepicker_mon = "div.ui-datepicker-group-first span.ui-datepicker-month"
    datepicker_yar = "div.ui-datepicker-group-first span.ui-datepicker-year"
    datepicker_next_mon ="div.ui-datepicker-group-last div a span"
    datepicker_prev_mon ="div.ui-datepicker-group-first div a span"

                            

class Result(object):
    hotel_name = "div.user-bar_hotelName"
    checkIn_date = '//button[@class="search-bar-container_checkIn"]/span[2]/span'
    checkOut_date = '//button[@class="search-bar-container_checkOut"]/span[2]'

    # promo_lable = '#code-Promotion-select lable'
    promo_textbox = "div.criteria-promo-codes_codes div.criteria-promo-codes_input input"

    menu_hotel_info = 'div#hotel-menu-flyout > button'
    smenu_hotel_details = 'div#hotel-menu-flyout > div ul li.hotel-info_menuHotelDetailsLink.new'
    hotel_details_des = 'div.descr.less'

class Book_secure_page(object):
    smenu_hotel_details = '//*[@id="fb-header-hotel"]/div[2]/div/span'
    hotel_details_title = '//*[@id="fb-hoteldetails-top"]/span'
