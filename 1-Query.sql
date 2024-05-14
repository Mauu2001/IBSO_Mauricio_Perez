SELECT
d.dnum as num_de_ticket, -- # de ticket -> FDOC -> DNUM
d.dfecha as fecha, -- Fecha -> FDOC -> DFECHA
d.dcant as monto_sin_iva, -- Monto (DCANT) con IVA -> FDOC -> DCANT
d.dcant * 1.16 as monto_con_iva, -- Monto (DCANT) sin IVA -> FDOC -> DCANT
d.dpar1 as vendedor, -- Vendedor -> FDOC -> DPAR1
c.clinom as cliente, -- Cliente -> FCLI -> CLINOM
i.ifam2 as productos_comprados -- Productos comprados (SKU) -> FINV -> IFAM2
i.idescr as despricion, -- Descripción -> FINV -> IDESCR
a.aicantf as cantidad, -- Cantidad (unidades) -> FAXINV -> AICANTF
a.ailmacen as almacen_que_vendio, -- Almacén que vendió -> FAXINV -> AIALMACEN
i.ilista3 as precio_de_lista, -- Precio de lista -> FINV -> ILISTA3
i.ifam3 as talla, -- Talla -> FINV -> IFAM3
i.ifam4 as color, -- Color -> FINV -> IFAM4
i.ifam5 as temporada -- Temporada -> FINV -> IFAM5
FROM fdoc d, faxinv a, finv i, fcli c
WHERE c.clicod = d.clicod
AND d.dnum = a.fmov
AND a.icod = i.icod