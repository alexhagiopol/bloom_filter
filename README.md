# Bloom Filter

### Implementation

I implemented a Hash Function class and a Bloom Filter class. Initializing the Bloom Filter requires passing the universe size N, the table size n, the database size m, and the number of hash functions k. Aside from its initialization, the Bloom Filter class has two functions: adding integers to the database and testing the database for the existence. When adding integers to the database, the Bloom Filter uses the Hash Function class to generate a hash index for the input integer. The Bloom Filter class then assigns a value of 1 to the hash index returned by the hash function. If the number of hash functions specified is greater than 1, then the Bloom Filter class creates k instances of the Hash Function class to generate k indices. When testing if an integer is in the Bloom Filter table, k hash function instances are created and k indices are generated. The Bloom Filter than checks the value at every index in the Bloom Filter table specified by the generated indices. If all values at the indices are equal to 1, then the tested value is said to be contained in the Bloom Filter database.

The Hash Function class is initialized by specifying an n value and a seed value. The n value represents the total size of the hash table to be used. The seed value is the random seed to be used to generate random hash values. Aside from its initialization, the hash function also has a getHashValue() function. When generating a random hash value, the hash function multiplies the given seed value by the value of the integer to be hashed. In this way, the hash function generates the same hash value for the same integer given the same random seed. This is useful when testing for the presence of the integer because every instance of the Bloom Filter has its own seed which it passes to each instance of Hash Function that it calls. 

### Testing

The Bloom Filter implementation was tested by writing a testing script that instantiated many, many Bloom Filters and tested insertion and recall. For different values of n and the same value of m, the testing script instantiated 10000 Bloom Filters and attempted insertion and recall of m database items. The number of hash functions k was set equal to (n/m)*ln(2) rounded to the nearest integer. On each of 10000 testing iterations for each value of n, a new Bloom Filter was instantiated with a different random seed. Then, a random number between 0 and m was chosen to not be added to the Bloom Filter table and every other number between 0 and m was added to the Bloom Filter table. After this was done, the Bloom Filter was tested for the presence of the integer not added to it. If the Bloom Filter test returns true meaning that the Bloom Filter thinks that it contains an integer not added to it, then we increment the measured number of false positives. 

### Results

As predicted by theory, the false positive frequency drops precipitously with increasing ratio between the table size and the database size so long as the number of hash functions k remains equal to (n/m)ln(2). Randomness in the data causes a somewhat non-monotonic drop in false positive percentage.

![Image Results Chart](https://github.com/alexhagiopol/BloomFilter/blob/master/results_chart.png)
![Image Results Chart](https://github.com/alexhagiopol/BloomFilter/blob/master/results_table.png)
