/*
1 find sum of each r card
*/
select r_creativity + r_decisionMaking + r_affinity + r_execution
from R
group by r_id


/*
2 find max sum
*/
select max(sum(r_creativity + r_decisionMaking + r_affinity + r_execution)),r_id
from R 


/*
3find the r cards that have most total values
*/
select r_name
from 
(
select max(sum) as m,r_id
from R ,
(select sum(r_creativity + r_decisionMaking + r_affinity + r_execution) as sum from R group by r_id)sql),
R
where (r_creativity + r_decisionMaking + r_affinity + r_execution) = m


/*
4find all the values of user's cards 
*/
select sr_creativity ,sr_decisionMaking ,sr_affinity , sr_execution,sr_name
from SR 
where sr_name = 'Temperature' or sr_name = 'Listen attentively'
union
select r_creativity ,r_decisionMaking ,r_affinity , r_execution,r_name
from R 
where r_name = 'After arrogance' or r_name = 'Dreamer'



/*
5compare is the score better than chapter requiments 
*/
select case when (r_creativity + r_decisionMaking + r_affinity + r_execution) > ﻿s_requireScore then 'TRUE' else 'FALSE' end
from R,stage,stageR 
where r_id = ﻿stgR_cardID and ﻿stgR_chapterNumber = ﻿﻿s_chapterNumber

/*
6 Order the difference between ssr and stage requirment
*/
select (ssr_creativity + ssr_decisionMaking + ssr_affinity + ssr_execution) - ﻿s_requireScore
from SSR,stage,stageSSR 
where ssr_id = ﻿stgSSR_cardID and ﻿stgSSR_chapterNumber = ﻿﻿s_chapterNumber
order by (ssr_creativity + ssr_decisionMaking + ssr_affinity + ssr_execution) - ﻿s_requireScore

/*
7 
*/
select ssr_name
from SSR
where ssr_name like 'l%' 

/*
8
*/
select count(hc_rid)
from heroineCards

/*
9
*/
﻿select r_name
from (
select r_name,sq1.max
from heroineCards,R,(select max(r_decisionMaking) as max from R )sq1
where hc_rid = r_id )

/*
10
*/
select distinct r_name ,hc_hid , (r_creativity + r_decisionMaking + r_affinity + r_execution)
from heroineCards,R
where hc_rid = r_id and hc_hid = '1'


1.
SELECT COUNT(r_id)
FROM R, Characters C
WHERE C.ch_id = R.r_chid
AND C.ch_name = 'ZEYAN LI'

2.
SELECT SUM(sq1.cnt_ssr + sq2.cnt_sr + sq3.cnt_r)
FROM (SELECT COUNT(DISTINCT ssr_id) AS cnt_ssr, SSR.ssr_chid FROM SSR) sq1,
(SELECT COUNT(DISTINCT sr_id) AS cnt_sr, SR.sr_chid FROM SR) sq2,
(SELECT COUNT(DISTINCT r_id) AS cnt_r, R.r_chid FROM R) sq3

3. Which company has greatest decisionMaking?
SELECT MAX(c.c_decisionMaking), c.c_name
FROM company c, heroine h
WHERE c.c_ID = h.h_companyID
LIMIT 1

4.
SELECT SSR.ssr_name, SSR.ssr_affinity
FROM SSR
ORDER BY ssr.ssr_affinity DESC

5. Which cards meets the requirements?
SELECT SR.sr_name
FROM stage s, SR, stageSR sSR
WHERE ((s.s_percentageA * SR.sr_affinity) +
(s.s_percentageC * SR.sr_creativity) +
(s.s_percentageDM * SR.sr_decisionMaking) +
(s.s_percentageE * SR.sr_execution)) >= s.s_requireScore
AND sSR.stgSR_cardID = SR.sr_id
AND sSR.stgSR_chapterNumber = s.s_chapterNumber
AND s.s_chapterNumber = '1.3'

6. top 3 cards to clear a stage:
SELECT SR.sr_name
FROM stage s, SR, stageSR sSR
WHERE ((s.s_percentageA * SR.sr_affinity) +
(s.s_percentageC * SR.sr_creativity) +
(s.s_percentageDM * SR.sr_decisionMaking) +
(s.s_percentageE * SR.sr_execution)) >= s.s_requireScore
AND sSR.stgSR_cardID = SR.sr_id
AND sSR.stgSR_chapterNumber = s.s_chapterNumber
AND s.s_chapterNumber = '1.3'
ORDER BY ((s.s_percentageA * SR.sr_affinity) +
(s.s_percentageC * SR.sr_creativity) +
(s.s_percentageDM * SR.sr_decisionMaking) +
(s.s_percentageE * SR.sr_execution)) DESC
LIMIT 3

7. The card with highest stats all sum up?
// Can replace the R with SR or SSR as desire.
SELECT MAX(sum_R)
FROM R,
(SELECT SUM(R.r_affinity + R.r_creativity + R.r_decisionMaking + R.r_execution) AS sum_R
FROM R
GROUP BY r.r_name)

8. Which character has the most number of SSR cards?
SELECT C.ch_name
FROM Characters C, SSR
WHERE SSR.ssr_chid = C.ch_id
GROUP BY C.ch_name
HAVING COUNT (SSR.ssr_id) =
(SELECT COUNT(SSR.ssr_id) AS num_cards
FROM Characters C, SSR
WHERE C.ch_id = SSR.ssr_chid
GROUP BY C.ch_name
ORDER BY num_cards
LIMIT 1)


9. SSR card that has the highest affinity?
// Output the card name, character name and the stat. Can replace with R or SR.
SELECT SSR.ssr_name, C.ch_name, SSR.ssr_affinity
FROM SSR, Characters C
WHERE SSR.ssr_affinity >= (SELECT MAX(SSR.ssr_affinity)
FROM SSR)
AND SSR.ssr_chid = C.ch_id

10. How much does company contribute?
SELECT MAX(sq1.num), c.c_name
FROM stageCompany sc, stage s, company c,
(SELECT SUM(c_affinity+c_creativity+c_decisionMaking+c_execution) * 0.2 AS num
FROM company
GROUP BY company.c_name
) sq1
WHERE sc.sc_companyID = c.c_ID
AND s.s_chapterNumber = sc.sc_chapterNumber

11. Find average stats for each element.
SELECT AVG(R.r_creativity + SR.sr_creativity + SSR.ssr_creativity) AS avg_c,
AVG(R.r_affinity + SR.sr_affinity + SSR.ssr_affinity) AS avg_a,
AVG(R.r_decisionMaking + SR.sr_decisionMaking + SSR.ssr_decisionMaking) AS avg_dm,
AVG(R.r_execution + SR.sr_execution + SSR.ssr_execution) AS avg_e, C.ch_name
FROM R, SR, SSR, Characters C
WHERE R.r_chid = C.ch_id
AND SR.sr_chid = C.ch_id
AND SSR.ssr_chid = C.ch_id
GROUP BY C.ch_name
































