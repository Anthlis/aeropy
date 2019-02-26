{% extends 'base.html' %}

{% block title %}AeroPy 2.0{% endblock %}

{% block page_content %}

<div class="jumbotron jumbotron-fluid">
<div class="container-fluid">
    <h3><font color="blue">Maths 21: Input with output!</font></h3>

    <form method=post action="">
        Hello, World! The sine of
        {{( form.r )}}
        <input type=submit value=equals>
        {% if s != None %}
        {{s}}
        {% endif %}
    </form>

</div>
</div>

{% endblock %}








