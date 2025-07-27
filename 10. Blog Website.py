from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory blog posts
posts = []


# Home page – show all posts
@app.route("/")
def index():
    return render_template_string(
        """
        <h1>My Simple Blog</h1>
        <a href="/add">Add New Post</a><br><br>
        {% for post in posts %}
            <div style="border:1px solid #ccc; padding:10px; margin-bottom:10px;">
                <h2>{{ post.title }}</h2>
                <p>{{ post.content }}</p>
            </div>
        {% else %}
            <p>No posts yet!</p>
        {% endfor %}
    """,
        posts=posts,
    )


# Add new post – GET form & POST data
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        posts.append({"title": title, "content": content})
        return redirect(url_for("index"))
    return render_template_string(
        """
        <h1>Add New Post</h1>
        <form method="POST">
            <input name="title" placeholder="Title" required><br><br>
            <textarea name="content" placeholder="Content" rows="5" cols="40" required></textarea><br><br>
            <button type="submit">Post</button>
        </form>
        <a href="/">Back to Blog</a>
    """
    )


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
