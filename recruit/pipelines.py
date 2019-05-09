import json
 
class RecruitPipeline(object):
    def open_spider(self,spider):
        self.file = open("position.text","w",encoding="utf-8")
    def process_item(self, item, spider):
        dict_item = dict(item)
        json_str = json.dumps(dict_item['position_title'],ensure_ascii=False)
        self.file.write('{\n\t'+'position_title:'+json_str+",\n")
        json_str = json.dumps(dict_item['position_link'],ensure_ascii=False)
        self.file.write("\n\tposition_link:"+json_str+",\n")
        json_str = json.dumps(dict_item['context_list'],ensure_ascii=False)+"\n"
        self.file.write("\n\tcontext_list:"+json_str+'},\n')
        return item
    def close_spider(self,spider):
        self.file.close()
