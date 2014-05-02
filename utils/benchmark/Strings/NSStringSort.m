#import <Foundation/Foundation.h>
#include <mach/mach_time.h>
#include <stdio.h>
// NOTE: compile with ARC enabled
// clang -fobjc-arc -O3 NSStringBench.m -o NSStringBench.bin -framework Foundation
#define LAPS 50

int
main(void) {
  NSArray *myArray = @[
 @"юношей",
 @"юриспруденции",
 @"юрковских",
 @"юлианские",
 @"юконам",
 @"юхансену",
 @"юлиных",
 @"юбилею",
 @"юнг",
 @"югорские",
 @"югославское",
 @"юрисконсульт",
 @"югорского",
 @"юнгфрау",
 @"юлианским",
 @"югорском",
 @"юбилярам",
 @"юнитах",
 @"юдищом",
 @"юбэнкс",
 @"юрием",
 @"югославском",
 @"югорская",
 @"юрине",
 @"юпитерианин",
 @"юджанка",
 @"юнговская",
 @"юмористический",
 @"юнионизма",
 @"юриспруденциям",
 @"юбилеями",
 @"юхансене",
 @"юргане",
 @"юхновского",
 @"юное",
 @"юлиям",
 @"юдище",
 @"юнгерам",
 @"юнкоровского",
 @"юрия",
 @"юнкерсе",
 @"юридическому",
 @"юххами",
 @"югославе",
 @"юнкерсах",
 @"юлей",
 @"юлившая",
 @"юриста",
 @"юнкерсами",
 @"юркому",
 @"юконах",
 @"юнга",
 @"юристов",
 @"югов",
 @"юхрим",
 @"юнону",
 @"юпитерианских",
 @"юрко",
 @"юбчонки",
 @"юнгу",
 @"юргенс",
 @"югре",
 @"юграми",
 @"юкка",
 @"юлькой",
 @"юговосточной",
 @"юджин",
 @"юланцу",
 @"юрашам",
 @"юкавы",
 @"юккам",
 @"юпитерианами",
 @"юлианов",
 @"югославским",
 @"юдиони",
 @"юнкерскее",
 @"юмора",
 @"юношескими",
 @"юньмень",
 @"юлианах",
 @"юнгере",
 @"юрганом",
 @"юридическего",
 @"юрковские",
 @"юдоре",
 @"юнкеру",
 @"юлить",
 @"юношестве",
 @"юниоры",
 @"юнис",
 @"юриям",
 @"юноше",
 @"юргам",
 @"юл",
 @"юговосточном",
 @"юмбо",
 @"юрганка",
 @"юмористического",
 @"юнкерскем",
 @"юрисдикцией",
 @"юбилеям",
 @"юлиусах",
 @"юбером",
 @"юпитерианскую",
 @"юмористах",
 @"юношества",
 @"юрганов",
 @"югорцы",
 @"юлана",
 @"юлиуса",
 @"юрина",
 @"юринелов",
 @"юркону",
 @"юморесками",
 @"юльках",
 @"юнаны",
 @"юнгами",
 @"юридическом",
 @"югам",
 @"юлькам",
 @"юрфаках",
 @"юралмед",
 @"юльке",
 @"югославскими",
 @"юпитерских",
 @"юньнань",
 @"юности",
 @"юбочкой",
 @"юргами",
 @"юкатане",
 @"юниверсал",
 @"юринеле",
 @"юлькинами",
 @"юхха",
 @"юлькина",
 @"юринов",
 @"юрганков",
 @"юбках",
 @"юркнулись",
 @"юхансенами",
 @"юргу",
 @"юношами",
 @"югославскому",
 @"юбиляру",
 @"юношеству",
 @"юрга",
 @"юношескую",
 @"юлькиное",
 @"югонам",
 @"юлиным",
 @"юргенов",
 @"юбочкам",
 @"юдифью",
 @"юлькиной",
 @"юнкерских",
 @"юнанов",
 @"юнгфюрер",
 @"юношеством",
 @"юланцам",
 @"юкатанам",
 @"юмористическим",
 @"юлу",
 @"юношеский",
 @"юлькиного",
 @"юрико",
 @"юпитеров",
 @"юлом",
 @"юлилось",
 @"юрисконсультам",
 @"юберу",
 @"юношеских",
 @"юринелу",
 @"югону",
 @"юбчонке",
 @"юрганкам",
 @"юхримов",
 @"юланца",
 @"юрмалам",
 @"юриных",
 @"юркое",
 @"юльку",
 @"юджанкам",
 @"юнкерами",
 @"юридичнов",
 @"юбиляров",
 @"юберлядено",
 @"юнус",
 @"юлиными",
 @"юнаньские",
 @"юргенсу",
 @"юрконам",
 @"юнец",
 @"юлит",
 @"юриспруденция",
 @"юланов",
 @"югославишь",
 @"юкон",
 @"юхансеном",
 @"юпитерах",
 @"юдищах",
 @"юнгой",
 @"юмивады",
 @"юбилеях",
 @"юниту",
 @"юрковскими",
 @"юлькинах",
 @"юная",
 @"юлианская",
 @"юнкерскего",
 @"юлий",
 @"юбчонках",
 @"юнгерах",
 @"юрка",
 @"юлькине",
 @"юкатанами",
 @"юнговские",
 @"юбилеи",
 @"юграм",
 @"юридичнами",
 @"юнцом",
 @"юрконе",
 @"юлиусе",
 @"югославия",
 @"юношом",
 @"юлькинов",
 @"юксиань",
 @"юливших",
 @"юлькиных",
 @"юлькину",
 @"юлиться",
 @"юрфаками",
 @"юмивадом",
 @"юдифи",
 @"юнкоровский",
 @"юристами",
 @"юрашов",
 @"юрашах",
 @"юранах",
 @"юмором",
 @"югорскими",
 @"юбками",
 @"юлиные",
 @"юберлядена",
 @"юморами",
 @"юлии",
 @"юдищами",
 @"юпитерам",
 @"юродивая",
 @"юмористическому",
 @"югославский",
 @"юридичнах",
 @"юриспруденцию",
 @"юркий",
 @"юнцам",
 @"юлиному",
 @"юдакова",
 @"юница",
 @"юношеском",
 @"юные",
 @"юли",
 @"юндо",
 @"юнану",
 @"юранами",
 @"юбиляром",
 @"юланец",
 @"юбочках",
 @"юриком",
 @"юджанком",
 @"юмористической",
 @"юберляденная",
 @"юджина",
 @"юного",
 @"юришевов",
 @"юришеву",
 @"юберляден",
 @"югорской",
 @"юнца",
 @"юпитериана",
 @"юрист",
 @"юишианы",
 @"юбкам",
 @"югославам",
 @"юлями",
 @"юньмэня",
 @"юбере",
 @"юлианцев",
 @"юр",
 @"юмах",
 @"юлдуз",
 @"юан",
 @"юришевом",
 @"югославская",
 @"юлькинам",
 @"юмористом",
 @"юринелом",
 @"юкуну",
 @"юргах",
 @"юмористы",
 @"юбилейного",
 @"юношествах",
 @"юхримом",
 @"юбочник",
 @"юхрима",
 @"юркнуло",
 @"юлькиная",
 @"юриного",
 @"югры",
 @"юрковская",
 @"юлиями",
 @"юнкерскими",
 @"юношу",
 @"юлианскее",
 @"юлианский",
 @"юлиус",
 @"юркнувших",
 @"юнцу",
 @"юрганами",
 @"юме",
 @"юными",
 @"юранов",
 @"югоном",
 @"югами",
 @"юнговским",
 @"юмор",
 @"югославов",
 @"юрфаке",
 @"юных",
 @"юркнуть",
 @"юлией",
 @"юхансенам",
 @"юном",
 @"юнкоры",
 @"юрии",
 @"юбчонком",
 @"юхансенах",
 @"юнанах",
 @"юлила",
 @"юханов",
 @"юриной",
 @"юристом",
 @"юпитерианской",
 @"юдоли",
 @"юконе",
 @"юкатанов",
 @"юнкеров",
 @"юридическим",
 @"юрмалов",
 @"юбилаумшахт",
 @"югославу",
 @"юргене",
 @"юдищов",
 @"юморок",
 @"юридическую",
 @"юнкерскему",
 @"юдищу",
 @"юбилеем",
 @"юнговской",
 @"юмов",
 @"юханам",
 @"юлькином",
 @"юнитами",
 @"юридичне",
 @"юркнулась",
 @"югозападном",
 @"юркая",
 @"юнкерская",
 @"юкатану",
 @"юнкоровская",
 @"юнкоровскими",
 @"югорских",
 @"юхримах",
 @"юпитерианином",
 @"юниорами",
 @"юнгеров",
 @"юпитериану",
 @"юлиев",
 @"югослава",
 @"юлившие",
 @"юберляденных",
 @"юхримам",
 @"юлькиный",
 @"юкунсам",
 @"юрисдикц",
 @"юриная",
 @"юнцов",
 @"юргенсов",
 @"юбок",
 @"юришевами",
 @"юнговских",
 @"юность",
 @"юноны",
 @"юххом",
 @"юханом",
 @"юпитериан",
 @"юлиях",
 @"юрмалом",
 @"юнкерсом",
 @"юлианцы",
 @"юджанках",
 @"юришева",
 @"юбилея",
 @"юмиваду",
 @"юргена",
 @"юморком",
 @"юкунсов",
 @"юной",
 @"юрковском",
 @"юманите",
 @"юга",
 @"юланце",
 @"юберлядены",
 @"юннаты",
 @"юхан",
 @"юрген",
 @"юриный",
 @"юморесок",
 @"юхриму",
 @"юлечка",
 @"юхриме",
 @"юрмалу",
 @"юдора",
 @"юлианом",
 @"юнонам",
 @"юлам",
 @"юриспруденциях",
 @"юбилейный",
 @"юпитерианам",
 @"юнцы",
 @"юххе",
 @"юркнувший",
 @"юлившим",
 @"юдовина",
 @"юмам",
 @"юра",
 @"юбилейные",
 @"юридическем",
 @"юбилей",
 @"юпитерианская",
 @"юбер",
 @"юрика",
 @"юмиваде",
 @"юхху",
 @"юнкером",
 @"юнитов",
 @"юджанку",
 @"юги",
 @"юнитам",
 @"юнаном",
 @"юморески",
 @"юбилейными",
 @"юдору",
 @"юдорах",
 @"юбчонка",
 @"юбалхо",
 @"юниоров",
 @"юнкерах",
 @"юлианович",
 @"юбки",
 @"юпитерианах",
 @"юпитерианина",
 @"юниформ",
 @"югославских",
 @"юниты",
 @"юнгера",
 @"юрмале",
 @"юнговскую",
 @"юрганам",
 @"юридические",
 @"юлиусом",
 @"юнион",
 @"юбилее",
 @"юбилейную",
 @"юмористику",
 @"юрию",
 @"юбилейное",
 @"юлька",
 @"юнгерами",
 @"юбчонками",
 @"юродивое",
 @"юпитерианину",
 @"юрганку",
 @"юнане",
 @"юристу",
 @"юнцами",
 @"юриным",
 @"юришевам",
 @"юпитерианом",
 @"юношов",
 @"юлил",
 @"юхансен",
 @"юленька",
 @"юхананов",
 @"юридичнам",
 @"юмивада",
 @"юринах",
 @"юрами",
 @"юрюнг",
 @"юрковский",
 @"юргенсам",
 @"югу",
 @"юмом",
 @"югославию",
 @"юниором",
 @"юрисконсультах",
 @"югозападе",
 @"юмористов",
 @"юлиного",
 @"юберам",
 @"юрик",
 @"юджанков",
 @"юньмэни",
 @"юбочки",
 @"юрконах",
 @"юнкерсу",
 @"юпитерианском",
 @"юринела",
 @"юджинам",
 @"юнце",
 @"югорское",
 @"юрганке",
 @"юнонов",
 @"юнкоровских",
 @"юпитерианский",
 @"юнана",
 @"юланами",
 @"юлианус",
 @"юлами",
 @"юльки",
 @"юпитер",
 @"юлианскего",
 @"юркие",
 @"юрком",
 @"юринелам",
 @"юпитерианинов",
 @"юргану",
 @"юристах",
 @"юлькиными",
 @"юниорской",
 @"юришеве",
 @"юниора",
 @"юлькиному",
 @"юла",
 @"юпитерианинах",
 @"юному",
 @"юнонах",
 @"юргов",
 @"юрана",
 @"юлило",
 @"юльевич",
 @"юг",
 @"юджанки",
 @"юримитси",
 @"юпитерианскими",
 @"юххам",
 @"юмору",
 @"юриками",
 @"югорским",
 @"юма",
 @"юланд",
 @"юкку",
 @"юкунсах",
 @"юридически",
 @"югон",
 @"юрконов",
 @"юбилейному",
 @"юля",
 @"юлиане",
 @"югославские",
 @"юго",
 @"юбчонкам",
 @"юбкой",
 @"юнона",
 @"юмивадах",
 @"юджанке",
 @"юге",
 @"юркнуться",
 @"юлиная",
 @"юрикам",
 @"юрмалах",
 @"юмореску",
 @"юрашом",
 @"юджинами",
 @"юнъэр",
 @"юланом",
 @"юрином",
 @"юбку",
 @"юрковское",
 @"юливши",
 @"юкках",
 @"юношескому",
 @"юкатан",
 @"юношество",
 @"юлию",
 @"юношествов",
 @"юдорами",
 @"юркнувшая",
 @"юрику",
 @"юпитере",
 @"юбков",
 @"юджинов",
 @"юрашу",
 @"юмористические",
 @"юлив",
 @"югославскую",
 @"юлианами",
 @"юхана",
 @"юконом",
 @"юбчонку",
 @"юхане",
 @"юдоазиата",
 @"юпитерианцев",
 @"юргана",
 @"юнгером",
 @"югозападной",
 @"юркона",
 @"юкунсе",
 @"юмивадами",
 @"юниоре",
 @"юморист",
 @"югославы",
 @"юньмэнями",
 @"юговостоке",
 @"юпитерианов",
 @"юриями",
 @"юношески",
 @"юлям",
 @"юмивадам",
 @"юпитерианец",
 @"юмористам",
 @"юморов",
 @"юбочек",
 @"юграх",
 @"юре",
 @"юберляденные",
 @"юкунса",
 @"юланцев",
 @"юлиану",
 @"юкона",
 @"юхансена",
 @"юмористе",
 @"юргенах",
 @"юркого",
 @"юланцами",
 @"юркнувшим",
 @"юденфрай",
 @"югославами",
 @"югоне",
 @"юпитериане",
 @"юриках",
 @"югославией",
 @"юдоров",
 @"юрисконсультами",
 @"юбилейных",
 @"юбилейной",
 @"юберах",
 @"юношеская",
 @"юрлов",
 @"юрфака",
 @"юльнула",
 @"юлю",
 @"юмористическими",
 @"юпитерианским",
 @"юргенами",
 @"юлане",
 @"юнкерсов",
 @"юлианскем",
 @"юлькины",
 @"юдо",
 @"юрисдикцию",
 @"югорскую",
 @"югорскому",
 @"юбочку",
 @"юбилейным",
 @"юркнула",
 @"юнгах",
 @"юдища",
 @"юнкоровские",
 @"юноноподобные",
 @"юлькиным",
 @"юджину",
 @"юркнувшей",
 @"юлившей",
 @"юным",
 @"юбке",
 @"юберляденный",
 @"югославах",
 @"юкики",
 @"юберляденной",
 @"юкки",
 @"юринелами",
 @"юриях",
 @"юргенсе",
 @"югонов",
 @"юморескам",
 @"юнге",
 @"юношеской",
 @"юриное",
 @"юланам",
 @"юбочке",
 @"юлианских",
 @"юньмэню",
 @"юристы",
 @"юлиана",
 @"юдищам",
 @"юрге",
 @"юрганком",
 @"юкатаном",
 @"юностью",
 @"югах",
 @"юрашей",
 @"юноной",
 @"юрисдикциями",
 @"юношам",
 @"юбком",
 @"юнкоровским",
 @"юниорах",
 @"юрковскому",
 @"юань",
 @"юрфаком",
 @"юраша",
 @"югославии",
 @"юните",
 @"юпитером",
 @"юрковского",
 @"югом",
 @"юлиусов",
 @"юргенсах",
 @"юраном",
 @"юнкерс",
 @"юрисдикциях",
 @"юпитерианинам",
 @"юрисконсульта",
 @"юпитерианскому",
 @"юрисдикции",
 @"юпитерианинами",
 @"юнкерсам",
 @"югославиями",
 @"юджанками",
 @"юрки",
 @"юльчетай",
 @"юньмэням",
 @"юланцов",
 @"юконской",
 @"юнчиков",
 @"юкатанах",
 @"юдоль",
 @"югославской",
 @"югославом",
 @"юморесках",
 @"юбилеев",
 @"юлькиные",
 @"юришевах",
 @"югославиях",
 @"юджине",
 @"юрконами",
 @"юххах",
 @"юбиляра",
 @"юлиный",
 @"юношествами",
 @"юрганках",
 @"юлиусами",
 @"юланцах",
 @"юрг",
 @"юристе",
 @"юрках",
 @"юркими",
 @"юишаны",
 @"юнкоровском",
 @"юрку",
 @"юлиан",
 @"юридичну",
 @"юнгам",
 @"юридический",
 @"юноном",
 @"юридическими",
 @"юлианам",
 @"юпитерианское",
 @"юридическая",
 @"юрану",
 @"юлеле",
 @"юрган",
 @"юпитеру",
 @"юмористических",
 @"юриными",
 @"юрисконсульту",
 @"югров",
 @"юнкерские",
 @"юрисдикциям",
 @"юркнув",
 @"юрике",
 @"юниорам",
 @"юньмэнь",
 @"юринами",
 @"югослав",
 @"юмористическая",
 @"юлившем",
 @"юношествам",
 @"юпитерианцы",
 @"юниору",
 @"юберами",
 @"юнгов",
 @"юношеские",
 @"юпитерианине",
 @"юкатана",
 @"юнитом",
 @"юноши",
 @"юлях",
 @"юмористами",
 @"юнговскими",
 @"юму",
 @"юморам",
 @"юкону",
 @"юдорам",
 @"юркой",
 @"юлианы",
 @"юнкоров",
 @"югром",
 @"юбочка",
 @"юлились",
 @"юнонами",
 @"юдифь",
 @"югонами",
 @"юпитерианские",
 @"юмористически",
 @"юрковским",
 @"юраше",
 @"юране",
 @"юливший",
 @"юркнулось",
 @"юденича",
 @"юргеном",
 @"юлианскими",
 @"юркнувшем",
 @"юрисдикция",
 @"юлах",
 @"юлилась",
 @"юнкер",
 @"юговосток",
 @"юхананова",
 @"юнги",
 @"юный",
 @"юранам",
 @"юргом",
 @"юхансенов",
 @"юлианскому",
 @"юриспруденцией",
 @"юбилярах",
 @"юдором",
 @"юнкерский",
 @"юрам",
 @"юнита",
 @"юкунсами",
 @"юркнувшие",
 @"югона",
 @"югорский",
 @"юрий",
 @"юридическему",
 @"юноша",
 @"юношах",
 @"юрисконсультом",
 @"юлия",
 @"юльками",
 @"юаней",
 @"юниверсити",
 @"юную",
 @"юринелах",
 @"юргенам",
 @"юбочками",
 @"юркнул",
 @"юкунсом",
 @"юлиусу",
 @"юношеского",
 @"юноне",
 @"юргенсами",
 @"юнгеру",
 @"юрфаков",
 @"юханах",
 @"юркнувшее",
 @"юньмэнях",
 @"юрке",
 @"юрины",
 @"югру",
 @"юрками",
 @"юбилейчик",
 @"юлиусам",
 @"юхану",
 @"юнкера",
 @"юнкерсы",
 @"юхримами",
 @"юланцом",
 @"юпитерами",
 @"юбка",
 @"юнкерским",
 @"юридично",
 @"юморе",
 @"юджином",
 @"юмореска",
 @"юнкоровское",
 @"юрфаку",
 @"югославиям",
 @"юнкерса",
 @"юнанам",
 @"юрисконсультов",
 @"юнайтед",
 @"юрашами",
 @"юридична",
 @"югославского",
 @"юрким",
 @"юриспруденциями",
 @"юпитерианского",
 @"юрганах",
 @"юнгер",
 @"юконов",
 @"юрких",
 @"юнгом",
 @"юридическое",
 @"юриному",
 @"юлианскему",
 @"юлили",
 @"юбчонков",
 @"юбилейном",
 @"юношеским",
 @"юлан",
 @"юмами",
 @"юмористическую",
 @"юрмала",
 @"юношеское",
 @"юморах",
 @"юмористическое",
 @"юханами",
 @"юлившее",
 @"юджинах",
 @"юрисконсульте",
 @"юристам",
 @"юнкере",
 @"юлиное",
 @"юлином",
 @"юнкоровскому",
 @"юмористическом",
 @"юридического",
 @"юбера",
 @"юнанами",
 @"юбиляре",
 @"юлану",
 @"юлой",
 @"юркую",
 @"юрах",
 @"юмористу",
 @"юбилярами",
 @"юриков",
 @"юмивадов",
 @"юридической",
 @"юргену",
 @"юркнувши",
 @"юркам",
 @"юридических",
 @"юдиштхира",
 @"юнговского",
 @"юконами",
 @"юридичном",
 @"юнчиковым",
 @"юрмалами",
 @"юпитера",
 @"юритмикс",
 @"юлов",
 @"юдовин",
 @"юрфакам",
 @"юламэм",
 @"юрин",
 @"юрконом",
 @"юлием",
 @"юргенсом",
 @"юланах",
 @"юргенса",
 @"юнцах",
 @"югонах",
 @"юкками",
 @"юран",
 @"юнгниккель",
 @"юкунс",
 @"юнеско",
 @"юмориста",
 @"юбчонкой",
 @"юрину",
 @"юле",
 @"юберов",
 @"юрганками",
 @"юнговский",
 @"юхнов",
 @"юридическее",
 @"юкунсу",
 @"юриные",
 @"югра",
 @"юришев",
 @"юххов",
 @"юркнули",
 @"юбилейная",
 @"юнкерам",
 @"юишиане",
 @"юринам"];

  uint64_t count = 0;
  uint64_t start = mach_absolute_time();
  for (unsigned i = 0; i < LAPS; i++) {
    [[myArray mutableCopy] sortUsingSelector: @selector(compare:)];
  }
  uint64_t delta = mach_absolute_time() - start;
  printf("%f ns\n",
 (double)delta);
  printf("%f ns/lap\n",
 (double)delta / (double)LAPS);
  return 0;
}
