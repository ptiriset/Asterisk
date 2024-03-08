
from string import Template
from Parser import Parser

class AsteriskVmFile:
    __conf_vm_t = Template('$rly_no => $vm_pw, $name, $name@rexcs\n') 

    
    def __init__(self, reg_lst, phone_lst):
        self.reg_lst = reg_lst
        self.phone_lst = phone_lst
        self.do_conf()
        
    def __write_files(self, f1, f2, c, s):
        # f1 -> main file
        # f2 -> secondary file
        # c -> check variable
        # s -> str to write to file
        # print("c: " + c + ". Str: " + s)
        f1.write(s)
        if (c != ""): f2.write(s)
        
    def __open_files(self, reg, ip_p, ip_s, exten):
        fp_name = reg + '-' + ip_p + '-voicemail.' + exten
        fp = open(fp_name, 'w') or die ('Cannot open file: ' + fp_name)
        fs_name = ""
        fs = ""
        if (ip_s != ""):
            fs_name = reg + '-b-' + ip_s + '-voicemail.' + exten
            fs = open(fs_name, 'w') or die ('Cannot open file: ' + fs_name)
        return fp, fs

    def do_conf(self):
        reg_gw_lst = [x for x in self.reg_lst]
        reg_gw_lst += [(x["name"], x["ipv4"], "") for x in Parser._ast["gateway"] ]
        #print(reg_gw_lst)
        for (reg, ip_p, ip_s) in reg_gw_lst:
            fp, fs = self.__open_files(reg, ip_p, ip_s, 'conf')
            self.__do_byte(fp, fs, ip_s)
            fp.close()
            if (fs != ''): fs.close()
                    
    def __do_byte(self, fp, fs, ip_s):
        self.__write_files(fp, fs, ip_s, "[rexcs]\n")
        byte_phones = [x for x in self.phone_lst if x["vm_pw"] != "" ]
        for b in byte_phones:
            s1 = self.__conf_vm_t.substitute({
                'name': b["name"],
                'vm_pw': b["vm_pw"],
                'rly_no': b["rly_no"]})
            self.__write_files(fp, fs, ip_s, s1)
        # end for
        self.__write_files(fp, fs, ip_s, "\n\n")
              
