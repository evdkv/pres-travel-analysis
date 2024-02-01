Data Dictionaries
==============================

The data dictionaries are below. **travel_raw** is the dataset scraped directly from
the U.S. Historian Website. **travel_tidy** is the dataset with separated locales and cleaned up dates.
**travel_processed** has the textual components cleaned up and ready for analyses.

travel_raw.csv
------------

• visit_type (chr): who visited a particular country (president/secretary)<br>
• name (chr): name of the president/secretary<br>
• country (chr): country visited<br>
• locale (chr): city/region visited, not separated<br>
• remarks (chr): the description of the visit provided by the U.S. Historian page<br>
• date (chr): date range of the visit<br>

travel_tidy.csv
------------

• event_id (int): An unique identifier for every remark<br>
• visit_type (chr): who visited a particular country (president/secretary)<br>
• name (chr): name of the president/secretary<br>
• country (chr): country visited<br>
• locale (chr): city/region visited, separated<br>
• remarks (chr): the description of the visit provided by the U.S. Historian page<br>
• date_start (date): The start of the visit<br>
• date_end (date): The end of the visit<br>

travel_processed.csv
------------

• event_id (int): An unique identifier for every remark<br>
• visit_type (chr): who visited a particular country (president/secretary)<br>
• name (chr): name of the president/secretary<br>
• country (chr): country visited<br>
• remarks (chr): the description of the visits, cleaned (lemamtized, no punctuation and other symbols)
