# Pop
> for Twitch ull_duck

말하면, 움직여요

## config.toml
- **fps**: 앱 fps 설정입니다. 높은 fps를 요구하지 않으므로 60으로 해주세요.
- **window**: 창 크기 설정입니다. 
기본 500x500이지만, 삽입할 이미지의 크기가 현재 창의 크기보다 크다면 바꾸어 주세요.
- **background**: 이미지 밖 배경 색 설정입니다.
RGB값을 차례대로 넣으면 됩니다. 기본색은 초록색(0 255 0)입니다.
- **recognition**: 소리 민감도 설정입니다.
마이크의 상황에 따라 유동적으로 설정하여 주세요.
- **duration**: 각 프레임별 시간 설정입니다.
ms단위(1s = 1000ms)이며, 꼭 프레임의 개수에 맞추어 설정하여 주세요.

## /images
프레임을 각각 저장하여 주세요. png파일만 호환됩니다.
> 1.png, 2.png, 3.png, ...

파일 명은 꼭 1부터 넣어주세요.

## render
이미지는 무조건 창의 정 가운데 위치하여 렌더링됩니다.
