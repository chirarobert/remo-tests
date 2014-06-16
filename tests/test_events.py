
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.create_event import CreateEvent
from pages.events import Events
from pages.event_detail import EventDetail
from pages.home import Home


class TestEvents:

    @pytest.mark.credentials
    def test_create_event(self, mozwebqa):
        home_page = Home(mozwebqa)
        home_page.login()
        events_page = home_page.header.click_events_link()
        create_event_page = events_page.click_create_event_button()

        #Create event with all required fields
        create_event_page.set_event_name("New Event")
        create_event_page.set_event_description("Fairly long description is required")
        create_event_page.set_event_venue("Mozilla office")
        create_event_page.set_event_venue_map()
        create_event_page.set_event_city("Mountain View")
        create_event_page.select_event_country("Antarctica")
        create_event_page.select_start_month("3")
        create_event_page.select_start_day("14")
        create_event_page.select_random_start_year()
        create_event_page.select_end_month("11")
        create_event_page.select_end_day("22")
        create_event_page.select_end_year("2022")
        create_event_page.set_event_category()
        create_event_page.select_estimated_attendance("100")
        create_event_page.set_event_success_metric("10")
        create_event_page.set_event_metric("2")
        create_event_page.set_event_success_metric2("20")
        create_event_page.set_event_metric2("3")
        create_event_page.set_event_goals()


        event_detail_page = create_event_page.click_save_event_button()

        Assert.true(event_detail_page.is_event_saved_message_visible)
        Assert.equal('New Event', event_detail_page.name)