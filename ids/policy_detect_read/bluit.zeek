export {
    redef enum Notice::Type += {
        attack_fpm,
    };
}

event tcp_packet(c: connection, is_orig: bool, flags: string, seq: count, ack: count, len: count, payload: string)
 {
 if ( is_orig && "mamku tvoyu" in payload )
            {
            local n: Notice::Info = Notice::Info($note=attack_fpm, 
                                                 $msg="attack fpm ", 
                                                 $sub=payload,
                                                 $conn=c);
            NOTICE(n);
            }

 }