cat zh/no_seg/zh.train.no_seg.tok | python break2radicals.py > zh/rad/zh.train.rad.tok
cat zh/no_seg/zh.dev.no_seg.tok | python break2radicals.py > zh/rad/zh.dev.rad.tok
cat zh/no_seg/zh.test.no_seg.tok | python break2radicals.py > zh/rad/zh.test.rad.tok