<?php


function getData($link, $categoryName)
{
$counter=0;
    $file = fopen("$categoryName.txt", "w");
    //print"STARTING NEW CATEGORY : $categoryName "."\n";

    while (true) {
        print"CATEGORY IS $categoryName and PAGE NUMBER  ".$counter."\n";
        if($counter==0){
            $data = file_get_contents($link."/");
        }
        else{
            $starter=1 + ($counter*25);
            $data = file_get_contents($link."__start--".$starter.".html");
        }

        preg_match_all('#\bhttps?://[^,\s()<>]+(?:\([\w\d]+\)|([^,[:punct:]\s]|/))#', $data, $match);
        $links = $match[0];


        $shopLinks = array();
        foreach ($links as $rowLink) {
            if (strpos($rowLink, 'https://rd.bizrate.com') !== false) {
                $parts = parse_url($rowLink);
                parse_str($parts['query'], $query);
                $shopLinks[] = $query['t'];
                fwrite($file, $query['t'] . "\n");
            }
        }

        $counter+=1;

        if(sizeof($shopLinks)==0){
            break;
        }


    }

    return;

    fclose($file);
}




$handle = fopen("links.txt", "r");
if ($handle) {
    while (($line = fgets($handle)) !== false) {



        $spliter=explode("/",$line);
        $line=$spliter[0]."/".$spliter[1]."/".$spliter[2]."/".$spliter[3]."/".$spliter[4]."/".$spliter[5];
        getData($line, trim($spliter[3]));
    }
    fclose($handle);
}


exit()












?>

