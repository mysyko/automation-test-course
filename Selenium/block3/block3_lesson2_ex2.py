def test(full_string, substring):
    index = full_string.find(substring)
    if index == -1: #if substring NOT found in the full_string
        print(f"expected {substring} to be substring of {full_string}")
    if index != -1: #if substring FOUND in the full_string
        print()

test('fulltext', 'fulltext')