import json

with open('my_papers.json', 'r') as file:
    data = json.load(file)

def format_authors(author_list):
    formatted = []
    for author in author_list:
        parts = author.split(', ')
        if len(parts) == 2:
            lastname, firstname = parts
            initial = firstname[0] + '.'
            formatted.append(f"{lastname}, {initial}")
        else:
            formatted.append(author)
    formatted = formatted[0:5]
    return ', '.join(formatted)

def make_entry(title, author_list, pub, pubdate, abstract, bibcode):
    authors = format_authors(author_list)
    new_abs = abstract[:250]
    return f"""
    <div class="publish-card">
        <div class="card-content-large">
            <h3>{title}</h3>
            <h4>{authors} et al.</h4>
            <h5>{pub}&emsp;•&emsp;{pubdate}</h5>
            <p>{new_abs}...</p>
            <p style="font-size:1.3em">
                <button class="button" style="padding: 0.7em; border-radius:50px">
                    <a href="https://ui.adsabs.harvard.edu/abs/{bibcode}/abstract"
                       style="text-decoration: none; font-size:1.1em;">View on ADS</a>
                </button>
            </p>
        </div>
    </div>
	"""

# Generate all entries
html_entries = []
for paper in data:
    entry = make_entry(
        title=paper.get('title', [''])[0],
        author_list=paper.get('author', []),
        pub=paper.get('pub', ''),
        pubdate=paper.get('pubdate', ''),
        abstract=paper.get('abstract', ''),
        bibcode=paper.get('bibcode', '')
    )
    html_entries.append(entry)

# Print or save
output = '\n'.join(html_entries)
print(output)

# Or save to file:
with open('publications.html', 'w') as f:
    f.write(output)