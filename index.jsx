import React from "react";

import { Text, Button } from "components";
import { useNavigate } from "react-router-dom";

const REPORTpopupPage = () => {
  const navigate = useNavigate();

  return (
    <>
      <div className="bg-gray_100 flex flex-col font-manrope items-center justify-start mx-[auto] p-[273px] sm:px-[20px] md:px-[40px] w-[100%]">
        <Text
          className="leading-[72.00px] text-center text-teal_900"
          as="h1"
          variant="h1"
        >
          <>
            If you have an URGENT <br />
            EMERGENCY
            <br />
            please call 9-1-1
          </>
        </Text>
        <div className="bg-red_700 h-[7px] md:px-[20px] w-[16%]"></div>
        <Button
          className="common-pointer bg-teal_900 cursor-pointer font-bold mb-[99px] min-w-[184px] mt-[83px] py-[21px] rounded-[4px] sm:text-[20px] md:text-[22px] text-[24px] text-center text-gray_100 w-[auto]"
          onClick={() => navigate("/report")}
        >
          CONTINUE
        </Button>
      </div>
    </>
  );
};

export default REPORTpopupPage;
