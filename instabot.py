from instapy import InstaPy
from instapy import smart_run

tags = [] # list of tags

username = '' # enter username
password = '' # enter password

session = InstaPy(username = username,
                  password = password,
                  headless_browser=False)

with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=1500,
                                    min_followers=50,
                                    min_following=50)

    session.set_do_follow(True, percentage=100)
    session.set_dont_like([]) # list of posts that you don't like

    session.like_by_tags(tags, amount=250)
