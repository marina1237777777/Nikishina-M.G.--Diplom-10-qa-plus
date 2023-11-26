-- noinspection SqlNoDataSourceInspectionForFile
Задание 1
SELECT cur.login,
COUNT(*)
FROM "Couriers" as cur
JOIN "Orders" as ord ON cur.Id = ord."courierId"
WHERE ord."inDelivery" = true
GROUP BY cur.login;



Задание 2
SELECT track,
   (CASE
          WHEN finished=true THEN 2
          WHEN cancelled=true THEN -1
          WHEN "inDelivery"=true THEN 1
      ELSE 0
      END) as status
 FROM "Orders" as ord;
