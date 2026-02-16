# QALang

**QANLang** (pronounced 'can-lang') is the backbone for QANotz QA data. It's designed to be human readable, with small tags so you can find your info easily.

```
{q 1 How do I center a div?
    {a 1 Use CSS display and justify
        {d c set display to flex and justify-content to center}
        {d h 1}}
    {a 2 Use CSS grid
        {d c set display to grid and place-items to center}
        {d h 0.8}}}
```

QANLang combines concepts from JSON, XML, and HTML into a single format.

---

## Key Components of QANLang

- **Top Level 'q' tag:** Write a new question by providing an index and a question. 
- **Secondary 'a' tag:** Write an answer to your question inside of a 'q' tag by providing an index and your answer.
- **Additional 'd' tags:** Metadata tags to give more information about your answer. Use different types like 'c' for comment, 'h' for helpfulness, and more.

---

## Why Not JSON?

QANLang was designed specifically for the quick edit style of note taking. While JSON is already powerful and widely used, it often requires additional formatting and syntax that slows that quick edit style.