import mechanize
import http.cookiejar

# Set Browser
br = mechanize.Browser()

# Set Cookie Jar
cj = http.cookiejar.LWPCookieJar()
br.set_cookiejar(cj)

# Set Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages? Just uncomment the following lines
# br.set_debug_http(True)
# br.set_debug_redirects(True)
# br.set_debug_responses(True)

# User-Agent (this is cheating, ok?) We are basically writing the headers to
# make it look like
# it's coming from a Firefox browser in Fedora
br.addheaders = [
    (
        "User-agent",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1",
    )
]

br.open("http://www.everytrail.com/guide/the-olomana-trail")

for y in br.links(url_regex="profile"):
    continue

# to get the last profile link in the html
print("http://everytrail.com" + y.url)  # since urls here are relative
