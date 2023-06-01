SELECT orgs_loc.org_name, country, region, zip, city, street_address, website 
FROM orgs_loc 
    JOIN orgs_info ON orgs_info.org_id = orgs_loc.org_id
    WHERE SUBSTR(zip,1,1) = '8';