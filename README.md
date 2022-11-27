# Italian Athletics Data Analysis

Developed by a fan of athletics and data, the goal of this project is to scrape historical Italian athletes' PB data as well as related information from the official [Italian Federation](https://www.fidal.it/graduatorie.php) rankings page.
The dataset contains over 900k entries of athletes' best performance on more than 20 track and field running events from 2005 to 2021.
Running events range from 60m to 100km on road covering indoors, outdoors, and road races.

This dataset is also available on [Kaggle](https://www.kaggle.com/datasets/davideliu/italian-athletics-historical-best-performances).

## Related blogs
- https://davideliu.com/2022/11/27/peak-performance-analysis-of-the-track-and-field-5000m-event/

## Dataset overview

The scraped data is saved in a `csv` format containing the following columns:
- Time: fastest time run by the athlete on a specific year.
- Wind: direction and strength of the wind if relevant.
- Name: name of the athlete.
- Birth year: date of birth of the athlete.
- Team: team the athlete is competing for.
- Position: final position in the event. This field can refer both to final of battery.
- Location: location of the event.
- Date: date of the event.
- Sex: gender of the athlete.
- Event: event name (e.g. 100m, 3000m, Marathon, ...).
- Type: can be indoor (I), outdoor (P), or road (S).

Scraped events include: 
- Indoor: 60m, 200m, 400m, 800m, 1500m, 3000m
- Outdoor: 100m, 200m, 300m, 400m, 800m, 1000m, 1500m, 3000m, 5000m, 10000m, 100m H, 110m H, 400m H, 3000m SC.
- Road: 5k, 10k, Halfmarathon, Marathon, 50k, 100k.

## How to 🏃‍♂️ the code
Install the required dependencies.
```bash
pip install -r requirements.txt
```
Run the scraper.
```bash
python scraper.py
```
Enjoy you data 😍

---

## Support
If you found this project interesting please support me by giving it a :star:, I would really appreciate it :grinning:
