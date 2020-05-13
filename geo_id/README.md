## Download Datasets in County Level

Probably we need to map it with the US FIPS ID, for example New York is equal to 36:

![US FIPS](https://github.com/Adamantia/covid19-mit-teamd004/blob/master/geo_id/us_fips.jpg?raw=true)


##  We choose the states among the top five biggest COVID-19 occurrences

### New York

![New York in US map](https://github.com/Adamantia/covid19-mit-teamd004/blob/master/geo_id/new_york.png?raw=true)


### New Jersey

![New Jersey in US map](https://github.com/Adamantia/covid19-mit-teamd004/blob/master/geo_id/new_jersey.png?raw=true)

### Massachusetts

![Massachusetts in US map](https://github.com/Adamantia/covid19-mit-teamd004/blob/master/geo_id/massachusetts.png?raw=true)

### Illinois

![Illinois in US map](https://github.com/Adamantia/covid19-mit-teamd004/blob/master/geo_id/illinois.png?raw=true)


### California 

![California in US map](https://github.com/Adamantia/covid19-mit-teamd004/blob/master/geo_id/california.png?raw=true)


## Example

Acessing the web page ([link](http://www.statsamerica.org/uscp/)), we can download the files if we now the FIPS code of each county that we want:

    <a href="javascript:output_link('36001', 'pt1', 'excel')"><img src="images/icons/excel16px.png" class="DownloadIcon" alt="Excel">Excel</a>  

 ### Decoding the link:

The id '36001' is a reference for (36 = New York FIPS code, and is 001 = Albany County).

'pt1' = The type of table that I am requesting (for example the demography one is pt2).

'excel' file format.
