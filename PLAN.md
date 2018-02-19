# Ideas for version 0.2

For systematization of information wiki approach works very well. 

Wiki pages in Wikipedia have any tags that can be added. See for example

https://en.wikipedia.org/wiki/Washington,_D.C.

We could enable wiki editing of the pages and allow arbitrary tags in intervention pages
with a requirement that these tags are described in corresponding page.
Locations could be treated as special tags that are required for any intervention page.

Three types of pages:

- location: /l/<location-slug>
- interventions: /l/<location-slug>/i/<intervention-slug>
- tag: /t/<tag-slug>

Intervention description would look like:

```
# Intervention title

General intervention description that can be edited as a wiki-document.

---

location: Washington
area: Public safety
type: Crime prevention
outcome: Reduce crime
website: https://ovsjg.dc.gov/service/private-security-camera-system-incentive-program
```

In version 0.2 we could have tags in the document. Later, we could allow adding tags via UI.
For example, similar to how it's done in OpenStreetMap:

https://www.openstreetmap.org/edit?node=158368533#map=17/38.90066/-77.05760
