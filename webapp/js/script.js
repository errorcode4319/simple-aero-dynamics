const canvas = document.getElementById('frame');
const ctx = canvas.getContext('2d');

const SPACING = 20;

// 벡터장 함수: 중심에서 방사형으로 퍼지는 벡터 생성
function calc_vector(x, y) {
    const centerX = canvas.width/2;
    const centerY = canvas.height/2;
    const dx = (x - centerX);
    const dy = (-(y - centerY));


    
    const polar_coord = convert_coord_cartesian2polar(dx, dy);
    const r = polar_coord.r;
    const c = polar_coord.c;

    console.log(`X: ${dx}, Y: ${dy} -> R: ${r}, C: ${c}`)

    let u = 0;
    let v = 0;

    let uv_list = []

    uv_list.push(uniform_flow(r, c, 1000))
    uv_list.push(vortex(r, c, 1700000))
    uv_list.push(doublet(r, c, 100000000))

    console.log(uv_list)
    
    for (uv of uv_list) {
        u = u + uv.u;
        v = v + uv.v; 
    }

    return {u: u, v: v};    
}

// 벡터 그리기 함수
function draw_vector(x, y, vec) {

    magnitude = Math.sqrt(vec.u**2 + vec.v**2);

    vec.u = vec.u / magnitude;
    vec.v = vec.v / magnitude;

    const scale = SPACING * 0.5;
    const endX = x + vec.u * scale;
    const endY = y + -vec.v * scale;
    
    // 벡터 본체
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(endX, endY);
    ctx.strokeStyle = 'blue';
    ctx.stroke();

    // 화살표 머리
    const angle = Math.atan2(-vec.v, vec.u);
    ctx.beginPath();
    ctx.moveTo(endX, endY);
    ctx.lineTo(endX - 4*Math.cos(angle-Math.PI/6), endY - 4*Math.sin(angle-Math.PI/6));
    ctx.lineTo(endX - 4*Math.cos(angle+Math.PI/6), endY - 4*Math.sin(angle+Math.PI/6));
    ctx.closePath();
    ctx.fillStyle = 'blue';
    ctx.fill();
}

// 전체 캔버스 초기화 및 벡터장 그리기

console.log("draw canvas")
ctx.clearRect(0, 0, canvas.width, canvas.height);
const spacing = SPACING;  // 벡터 간격
for(let x=spacing/2; x<canvas.width; x+=spacing) {
    for(let y=spacing/2; y<canvas.height; y+=spacing) {
        const vec = calc_vector(x, y);

        console.log(vec)

        draw_vector(x, y, vec);
    }
}