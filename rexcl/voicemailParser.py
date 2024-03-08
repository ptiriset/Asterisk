
from RexclException import ParsingError
from Parser import Parser
from PhoneParser import PhoneParser

class voicemailParser(Parser):
    def __init__(self, line_no, line):
        Parser.__init__(self, line_no, line)
        self.match_token("vm")
        self.match_token("(")
        vm_pw = self.get_token()
        self.match_token(",")
        phone = self.get_token()
        self.match_token(")")
        self.check_for_extra_chars()
        
        for v in Parser._ast["phone"]:
            if v["name"] == phone:
                v["vm_pw"] = vm_pw
                return
            # end if
        # end for
        # I am here. This means that the phone does not exist
        raise ParsingError("Phone " + phone +
                              " not defined. " +
                              self.error_string())
