# Generates the HTML for a project for insertion into the pages section of the website
# Samuel May 2019


title = str(input("Title of the project: "))
description = str(input("Description: "))
relHeaderPath = str(input("Relative path of the header image: "))
githubLink = str(input("Github link: "))
pageLink = str(input("Relative page link: "))

output = """

<!-- {0} project card -->
<div class="col-lg-4 prj-card">

    <!-- Tags -->
    <a href='{3}' id='code-link' class='bg-success text-light'>Github</a>
    <a href='{4}' id='info-link' class='bg-info text-light'>Write-up</a>

    <!-- Header Image -->
    <img src='{2}' alt=''>

    <div class='content-divide bg-light'>

        <!-- Title and text -->

        <p class='display-4'>{0}</p>
        <p>{1}</p>

        <!-- Outbound links at the bottom of the page -->
        <div class='outbound-container'>
            <div class='outbound-link bg-success'>
                <a href='{3}'>Github</a>
                <a><img href='{3}' src='res/arrow.png'></a>
            </div>
            <div class='outbound-link bg-info'>
                <a href='{4}'>Write-up</a>
                <a href='{4}'><img href='#' src='res/arrow.png'></a>
            </div>
        </div>
    </div>
</div>
"""

print(output.format(title, description, relHeaderPath, githubLink, pageLink))


