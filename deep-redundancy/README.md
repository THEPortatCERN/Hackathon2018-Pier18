# Identifying Redundancy

> The project is assumed to be in home folder as "deep-redundancy"
> The data is assumed to be at ~/deep-redundancy/data/deep.csv

1. Get the csv data from deep
    - Fix the data encoding for the csv if needed using fix.py
    - Transform the csv (text has raw text as well as html) into json using transform.py

    ```
    cd ~/deep-redundancy
    fix.py > ./data/deep.csv
    transform.py > ./data/deep.json
    ```

2. Install solr inside `~/deep-redundancy` and start it

```
cd ~/deep-redundancy/solr
./bin/solr start
```
3. Setup solr  for deep (Go inside the solr directory)

```
./bin/solr create -c deep -s 2 -rf 2\
curl -X POST -H 'Content-type:application/json' --data-binary '{"add-field": {"name":"title", "type":"text_general", "multiValued":false, "stored":true}}' http://localhost:8983/solr/deep/schema
curl -X POST -H 'Content-type:application/json' --data-binary '{"add-field": {"name":"text", "type":"text_general", "multiValued":false, "stored":true}}' http://localhost:8983/solr/deep/schema
curl -X POST -H 'Content-type:application/json' --data-binary '{"add-field": {"name":"published_date", "type":"text_general", "multiValued":false, "stored":true}}' http://localhost:8983/solr/deep/schema
curl -X POST -H 'Content-type:application/json' --data-binary '{"add-field": {"name":"publisher", "type":"text_general", "multiValued":false, "stored":true}}' http://localhost:8983/solr/deep/schema
curl -X POST -H 'Content-type:application/json' --data-binary '{"add-copy-field" : {"source":"*","dest":"_text_"}}' http://localhost:8983/solr/deep/schema
```

> You can check out the solr dashboard at http://localhost:8983/solr/#/deep/query

4. Load data

```
./bin/post -c deep ~/deep-redundancy/data/deep.json
```

5. Open visualization
```
cd ~/deep-redundancy/visualization
python2 -m SimpleHTTPServer 8888 &
```

> You will need to disable CORS in the browser to query the solr server for now.
