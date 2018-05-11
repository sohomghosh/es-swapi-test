#group by, aggregate operator
res= es.search(index='megacorp',doc_type='employee',body={
        "aggs": {
            "all_interests": {
            "terms": { "field": "interests" }
            }
        }
    })


#other elastic search examples
#https://qbox.io/blog/python-scripts-interact-elasticsearch-examples
