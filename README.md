<body><h1>htm-dsl</h1><p>This is a simple DSL that generates HTML from python. Constructing a HTML document is a matter of nesting functions.
<pre>
html(
    head(title("Some webpage")),
    body(
        h1("Title"),
        p(
            "Freely mixing strings with ",
            code("htm-dsl"),
            " functions allows you to interpolate tags in text.",
            br(),
            "Keyword arguments are used to create attributes, like ",
            a("this!", href="https://github.com/delucks/htm-dsl")
        )
    )
)</pre><br></br>For an example, look at <code>README.py</code>, which generates this README!</p></body>
