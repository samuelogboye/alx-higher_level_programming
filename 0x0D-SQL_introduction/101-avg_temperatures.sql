-- a script that displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending)
SELECT `city`, AVG(`values`) AS `av_temp`
FROM `temperatures
GROUP BY `city`
ORDER BY `av_temp` DESC;
