process_pages = True

# Whether HTTP parsing should allow a trailing semicolon in the media type.
# Such a semicolon would violate the protocol, but they are sometimes seen in
# practice.
allow_trailing_semicolon = True

# Whether HTTP parsing should case whether the content length matches the
# content-length header.
strict_http_parse_body = True

# Whether to pad missing data in TCP flows with 0 bytes
pad_missing_tcp_data = True
