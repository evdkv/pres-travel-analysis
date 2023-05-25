Data Dictionaries
==============================

The data dictionaries are below. **travel_raw** is the dataset scraped directly from
the U.S. Historian Website. **travel_tidy** is the dataset with separated locales and clened up dates.
**travel_processed** has the textual components cleaned up and ready for analyses.

travel_raw.csv
------------

• visit_type (chr): who visited a particular country (president/secretary)
• name (chr): name of the president/secretary
• country (chr): country visited
• locale (chr): city/region visited, not separated
• remarks (chr): the description of the visit provided by the U.S. Historian page
• date (chr): date range of the visit

travel_tidy.csv
------------

• event_id (int): An unique identifier for every remark
• visit_type (chr): who visited a particular country (president/secretary)
• name (chr): name of the president/secretary
• country (chr): country visited
• locale (chr): city/region visited, separated
• remarks (chr): the description of the visit provided by the U.S. Historian page
• date_start (date): The start of the visit
• date_end (date): The end of the visit

travel_processed.csv
------------

• event_id (int): An unique identifier for every remark
• visit_type (chr): who visited a particular country (president/secretary)
• name (chr): name of the president/secretary
• country (chr): country visited
• remarks (chr): the description of the visits, cleaned (lemamtized, no punctuation and other symbols)