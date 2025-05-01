function convert_coord_cartesian2polar(x, y) {
    const r = Math.sqrt(x**2 + y**2);
    const c = Math.atan2(y, x);
    return {r: r, c: c};
}

function conv_velocity_polar2cartesian(r, c, v_r, v_c) {
    const u = v_r * Math.cos(c) - v_c * Math.sin(c)
    const v = v_r * Math.sin(c) + v_c * Math.cos(c)
    return {u: u, v: v}
}

function uniform_flow(r, c, velocity) {
    return {u: Number(velocity), v: 0};
}

function source(r, c, strength) {
    if (r === 0) {
        return {u: 0, v: 0};
    }
    
    v_r = Number(strength) / (2 * Math.PI * r);   
    v_c = 0;

    console.log(v_r, v_c)
    
    return conv_velocity_polar2cartesian(r, c, v_r, v_c);
}

function sink(r, c, strength) {
    return source(r, c, -strength);
}

function vortex(r, c, circulation) {
    if (r === 0) {
        return {u: 0, v: 0};
    }

    v_r = 0.0
    v_c = -circulation / (2 * Math.PI * r)
    
    return conv_velocity_polar2cartesian(r, c, v_r, v_c);
}

function doublet(r, c, moment) {
    if (r === 0) {
        return {u: 0, v: 0};
    }

    v_r = (-moment * Math.cos(c)) / (2 * Math.PI * (r**2));
    v_c = (-moment * Math.sin(c)) / (2 * Math.PI * (r**2));
    
    return conv_velocity_polar2cartesian(r, c, v_r, v_c);
}

function get_uv_offset_list(r, c) {
    
    let uv_list = [];

    const calc_list = [
        {check_id: "check_uniflow", val_id: "uniflow_val", func: uniform_flow, val_scale: 10},
        {check_id: "check_source", val_id: "source_val", func: source, val_scale: 100},
        {check_id: "check_sink", val_id: "sink_val", func: sink, val_scale: 100},
        {check_id: "check_vortex", val_id: "vortex_val", func: vortex, val_scale: 100},
        {check_id: "check_doublet", val_id: "doublet_val", func: doublet, val_scale: 50000},
    ];

    for (calc of calc_list) {
        const check = document.getElementById(calc.check_id);
        const val = document.getElementById(calc.val_id);
        if (check.checked) {
            uv_list.push(calc.func(r, c, Number(val.value) * calc.val_scale));
        }
    }

    return uv_list;
}