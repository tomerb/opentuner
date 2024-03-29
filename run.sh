#!/bin/bash

test_limits=(10 100 1000)
dimensions_list=(2 3 4 5 6 7 8 9 10)
domain_list=(5 10 100 250 500 750 1000 1500)

# Loop through each domain
for domain in "${domain_list[@]}"; do
    echo "Running with domain $domain"

    # Loop through each dimension
    for dimensions in "${dimensions_list[@]}"; do
        echo "    Running with dimensions $dimensions"
        
        # Loop through each test limit
        for limit in "${test_limits[@]}"; do
            echo "        Running with test limit $limit"
            python examples/rosenbrock/rosenbrock.py --test-limit "$limit" --dimensions "$dimensions" --domain "$domain" --metric-log "metric-data.csv"
        done
    done
    
    echo "-------------------------------------------"
done
