import datetime
from behave import step


@step("Open the url {url}")
def go_to_url(context, url):
    sb = context.sb
    sb.open("https://fareasthospitalitydev.brayleinosplash.com/")
    sb.maximize_window()

@step(u'Close the popup')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given Close the popup')
    sb = context.sb
    sb.click("//div[@class='modal-dialog']//div[@class=' modal-inner ']/button")

@step(u'Click on Book Now CTA')
def step_impl(context):
    sb = context.sb
    sb.click("//nav[@class='navbar navbar-default']//div[@class='desktop-only']//a[@id='top-book-now']")

@step(u'Booking wedget is display')
def step_impl(context):
    booknow_wg ='div.desktop-only > div >div.grey-bg:nth-child(1)'
    sb = context.sb
    sb.assert_element(booknow_wg)


@step(u'I select Location "Singapore"')
def step_impl(context):
    location ="div.desktop-only > div >div.grey-bg:nth-child(1) button[data-id='location']"
    singapore = "div.desktop-only > div >div.grey-bg div.location  li[data-original-index='1']"
    sb = context.sb
    sb.click(location)
    sb.click(singapore)
@step(u'Select Hotel "Oasia Hotel Downtown"')
def step_impl(context):
    sb = context.sb
    property ="div.desktop-only > div >div.grey-bg:nth-child(1) button[data-id='property']"
    OasiaHotelDowntown = "div.desktop-only > div >div.grey-bg div.property  li[data-original-index='1']"
    # sb.click(property)
    # sb.sleep(5)
    sb.click(OasiaHotelDowntown)

@step(u'Select Check In Date is TODAY')
def step_impl(context):
    sb = context.sb
    checkin_field = 'div.desktop-only > div >div.grey-bg input.checkin-date'
    # sb.type(checkin_field,"29 May 2023")
    sb.click(checkin_field)
    # table.ui-datepicker-calendar td[data-month='4'][data-year='2023'] a[data-date='29']
    today = datetime.date.today()
    day = today.day
    month = today.month
    year = today.year
    day_locator = f"table.ui-datepicker-calendar td[data-month='{month}'][data-year='{year}'] a[data-date='{day}']"
    sb.click(day_locator)

@step(u'Select Check Out is TODAY + 2')
def step_impl(context):
    sb = context.sb
    today = datetime.date.today() + datetime.timedelta(days=2)

    day = today.day
    month = today.month
    year = today.year
    
    day_locator = f"table.ui-datepicker-calendar td[data-month='{month}'][data-year='{year}'] a[data-date='{day}']"
    sb.click(day_locator)


@step(u'Enter number of Guests "{nAdult}" Adult(s), "{nChild}" Child(ren)')
def step_impl(context,nAdult, nChild):
    sb = context.sb
    # bt_minus_sign ="div.desktop-only > div >div.grey-bg li.adults-block span.minus-sign"
    # bt_plus_sign = "div.desktop-only > div >div.grey-bg li.adults-block span.plus-sign"
    
    # lb_adultlable= "div.desktop-only > div >div.grey-bg span.adultsLabel"
    # max_N = sb.get_attribute(lb_adultlable,"data-max-pax-limit")
    # min_N = sb.get_attribute(lb_adultlable,"data-min-limit")
    # currect_number = sb.get_text(lb_adultlable)

    # while nAdult != currect_number:
    #     sb.click(bt_plus_sign) if nAdult > currect_number else sb.click(bt_minus_sign)
    #     currect_number = sb.get_text(lb_adultlable)

    children =  "div.desktop-only > div >div.grey-bg li.children-block"
    adult = "div.desktop-only > div >div.grey-bg li.adults-block"
    choose_numb_of(sb ,adult, nAdult)
    choose_numb_of(sb, children,nChild)

# @step(u'Choose number of')  
def choose_numb_of(self, selector, numb):
    
    bt_minus_sign =f"{selector}> span:nth-child(1)"
    bt_plus_sign = f"{selector}> span:nth-child(3)"
    lb_numb = f"{selector} span.occ-label"

    max_N = self.get_attribute(lb_numb,"data-max-pax-limit")
    min_N = self.get_attribute(lb_numb,"data-min-limit")

    currect_number = self.get_text(lb_numb) 
    while numb != currect_number:
        self.click(bt_plus_sign) if numb > currect_number else self.click(bt_minus_sign)
        currect_number = self.get_text(lb_numb)



@step(u'Check Availability is enable')
def step_impl(context):
    pass


@step(u'I click on Check Availability')
def step_impl(context):
    sb = context.sb
    bt_checkAvailability = "div.desktop-only > div >div.grey-bg button.check-availability-btn"
    sb.click(bt_checkAvailability)

@step(u'I should navigate to "{title}" page')
def step_impl(context, title):
    sb = context.sb
    sb.assert_title(title)
    # raise NotImplementedError(u'STEP: Then I should navigate to "{title}" page')


@step(u'Verify the hotel name is "{hotelName}"')
def step_impl(context,hotelName):
    sb = context.sb

    sb.switch_to_window(1)
    print(sb.get_title())
    lb_hotel_name =  "div.user-bar_hotelName"
    full_hotel_name = sb.get_text(lb_hotel_name)
    # sb.assert_text(hotelName,lb_hotel_name)
    sb.assert_true(hotelName.upper() in full_hotel_name, f"hotel name is {full_hotel_name} don't match with {hotelName}")

    # Oasia Hotel Downtown by Far East Hospitality
    


@step(u'Verify number of Guests')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then Verify number of Guests')
    # button.search-bar-container_guests span:nth-child(2) -- adult numbert
    # button.search-bar-container_guests span:nth-child(3) -- child numbert
    pass


@step(u'Verify Check In Date')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then Verify Check In Date')
    pass

@step(u'Verify checkout Date')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then Verify checkout Date')
    pass