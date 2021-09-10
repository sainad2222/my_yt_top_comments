import os
import googleapiclient.discovery
from bs4 import BeautifulSoup
from tqdm import tqdm

"""
params:
    id: CommentId(String)
returns:
    -1, if error
    likes count, otherwise
"""


def likes(id):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.getenv("API_KEY") or "INSERT_YOUR_API_KEY"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    request = youtube.comments().list(part="snippet", id=id)
    try:
        response = request.execute()
    except Exception as e:
        print(e, id)
        return -1
    if len(response["items"]) == 0:
        return -1
    try:
        return response["items"][0]["snippet"]["likeCount"]
    except Exception as e:
        print(e, id)
        return -1


f = open("my-comments.html", "r")
out = open("results.html", "w")
out.write(
    """
        <head>
        <title>Top Comments</title>
        </head>
        <body>
        <table>
        <tr>
        <th>likes </th>
        <th>Video </th>
        <th>Comment </th>
        </tr>
        """
)
soup = BeautifulSoup(f, features="html.parser")
comments = soup.find_all("li")
result = []
for comment in tqdm(comments):
    commentLink = comment.a.attrs["href"]
    commentContent = comment.contents[-1]
    commentId = commentLink[commentLink.find("lc=") + 3 :]
    k = likes(commentId)
    if k == -1:
        continue
    result.append([k, commentLink, commentContent])
result = sorted(result, reverse=True)
#  replace 10 with any number
for likes, link, content in result[:10]:
    out.write(
        f"""
            <tr>
            <td>{likes}</td>
            <td><a href='{link}'>Video</a></td>
            <td>{content}</td>
            </tr>
            """
    )
out.write(
    """
        </table>
        </body>
        """
)
f.close()
out.close()
