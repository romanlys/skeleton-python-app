from queryprocessor import process_query

def test_knows_who_wrote_romeo_and_juliet():
	assert process_query("Who wrote Romeo and Juliet") == "William Shakespeare"

def test_is_case_insensitive():
	assert process_query("Who wrote romeo and JULIET") == "William Shakespeare"

def test_returns_empty_string_if_cannot_process_query():
	assert process_query("xxxx") == ""
