# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest import GaiaTestCase
from gaiatest.apps.browser.app import Browser


class TestBrowserSearch(GaiaTestCase):

    _bing_search_input_locator = ('name', 'q')

    def setUp(self):
        GaiaTestCase.setUp(self)
        self.connect_to_network()

    def test_browser_search(self):
        # https://github.com/mozilla/gaia-ui-tests/issues/451
        browser = Browser(self.marionette)
        browser.launch()

        search_text = 'Mozilla Web QA'

        browser.go_to_url(search_text)

        browser.switch_to_content()
        self.wait_for_element_displayed(*self._bing_search_input_locator)
        self.assertTrue(search_text in self.marionette.title)
        self.assertEqual(search_text,
                         self.marionette.find_element(*self._bing_search_input_locator).get_attribute('value'))
