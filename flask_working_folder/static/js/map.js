// create layer groups based on year (FIRE_YEAR), fire size class (FIRE_SIZE_CLASS)
// have year layer group be controlled by slider -- leaflet slider
// have fire size be in the drop down menu

// bind pop up with fire start date (DISCOVERY_DATE) and acres burned (FIRE_SIZE)
// bubbles are colored based on fire classification (FIRE_SIZE_CLASS)


// create for loop to sort through data
//      conditonals to check each year
//          push each fire to their respective years
//      conditionals to check each fire size class
//          push each fire to their respective classes 
//      

const sqlite3 = reuire("sqlite3").verbose();

//open database 
let data = sqlite3.Database('./data.sqlite');

