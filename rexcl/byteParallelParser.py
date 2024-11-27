
from RexclException import ParsingError
from Parser import Parser
from PhoneParser import PhoneParser

class byteParallelParser(Parser):
    def __init__(self, line_no, line):
        Parser.__init__(self, line_no, line)
        self.match_token("byteparallel")
        self.match_token("(")
        byte_parallel1 = self.get_token()
        self.match_token(",")
        byte_parallel2 = self.get_token()
        self.match_token(",")
        phone = self.get_token()
        self.match_token(")")
        self.check_for_extra_chars()
        
        for v in Parser._ast["phone"]:
            if v["name"] == phone:
                v["byte_parallel1"] = byte_parallel1
                v["byte_parallel2"] = byte_parallel2
                
                return
            # end if
        # end for
        # I am here. This means that the phone does not exist
        raise ParsingError("Phone " + phone +
                              " not defined. " +
                              self.error_string())
