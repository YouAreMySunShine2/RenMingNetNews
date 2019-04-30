import json
 
class RecruitPipeline(object):
    def open_spider(self,spider):
        self.file = open("position.text","w",encoding="utf-8")
    def process_item(self, item, spider):
        dict_item = dict(item)
        json_str = json.dumps(dict_item,ensure_ascii=False)+"\n"
        self.file.write(json_str)
        return item
    def close_spider(self,spider):
        self.file.close()
