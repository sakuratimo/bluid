export {
    redef enum Notice::Type += {
        attack_read,
    };
}

event tcp_packet(c: connection, is_orig: bool, flags: string, seq: count, ack: count, len: count, payload: string)
 {
 if ( is_orig && "plugin-backup-download?file=../" in payload )
            {
            local n: Notice::Info = Notice::Info($note=attack_read, 
                                                 $msg="attack read ", 
                                                 $sub=payload,
                                                 $conn=c);
            NOTICE(n);
            }

 }