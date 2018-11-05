# Department of Cultural Affairs - Neighborhood Arts Profile + Cultural Activity Analysis

## About

The City of Los Angeles Department of Cultural Affairs (DCA) is currently developing the Neighborhood Arts Profile, a research tool that assesses arts and cultural vibrancy in each of the City’s 100+ neighborhoods. With this tool, we identify “arts deserts,” locating areas of concentration and scarcity of infrastructural support for cultural assets and activities, alongside community wellbeing indicators. This pursuit of neighborhood-level insights will inform our place-based strategy toward building city-wide community vibrancy.

As a part of the [ Neighborhood Arts Profile](https://neighborhoodartsprofile.org/) (NAP), we would like to develop a data transformation and analytic model to map LA’s cultural activities. 

Working with a DSF partner, we plan to: 

1. implement programmatic methods to extract, aggregate, and structure existing cultural activities data sources made available through events curation apps and websites including: [ DiscoverLA](https://www.discoverlosangeles.com), [ CurateLA](https://curate.la/), [ ForYourArt](http://foryourart.com/), [ The CultureList](http://theculturelist.org/), [ Sea Saw](https://itunes.apple.com/us/app/see-saw-gallery-guide/id791643418?mt=8), [ LA Weekly](https://www.laweekly.com/), [ Los Angeles Public Library Calendar](www.lapl.org/whats-on/calendar), [ Eventbrite API](https://www.eventbrite.com/developer/v3/endpoints/events/#ebapi-get-events-search), and [ DCA’s events](https://culturela.org/wp-json/events/v1/dca-events/) ([Click here](https://docs.google.com/document/d/11xU03oyUEvchKiHgG_z1wV7EtG1W0FmsqUtWS8ja9oc/edit?usp=sharing) for the documentation for the events API); 

and

2. create an analytic model to index events data as a means to assess cultural vibrancy across Los Angeles neighborhoods.

## Sponsors

Danielle Brazell, DCA

Jeanne Holm, ITA

## Partners

Pomona College

## City Team

Umi Hsu

Hunter Owens

Christine Nguyen

## Goals

* Develop a script to aggregate and structure existing cultural activities data sources made available by apps and websites that can be run and remain up to date. The focus of this project phase should be aggregation and aligning existing data sources since some data sources are already structured as API (JSON feed as in the case of DiscoverLA and soon to be case by LAPL). 

* Perform exploratory analysis to rank neighborhood-level cultural vitality levels by assessing arts events data. 

* Provide preliminary analytic results on neighborhoods with high and low levels of cultural vibrancy based on DCA’s mission.

* Provide preliminary analytic results on neighborhoods with high and low levels of cultural vibrancy based on DCA’s mission.

  * Access to public transit (1 mile walking distance to mass transit stop)

  * Financial access: free and low-cost events

  * Access to youth: youth-specific and family-friendly events

## Deliverables

* Webscraper scripts that aggregate and structure data for analysis. Documentation on Github.

* A report on the results of preliminary analysis with interactive visualizations (can provide access to mapping tool related to project) and underlying data to DCA staff. This report should also document analytics methods. 

## Data Sources

* [DiscoverLA JSON feed](https://www.discoverlosangeles.com/feeds/events/dept-cultural-affairs/calendar)

* LA Public Library JSON feed [ Kids & Teens](http://www.lapl.org/whats-on/calendar/json/ita-kids-teens); [ All ages](http://www.lapl.org/whats-on/calendar/json/ita-all-ages)

* [Eventbrite API](https://www.eventbrite.com/developer/v3/endpoints/events/#ebapi-get-events-search)

* DCA events JSON feed (TBA)

## Timeline/Sprints

Fall semester: data transformation; methods documentation
Spring semester: analytic model development, full report


