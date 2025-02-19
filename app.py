import streamlit as st
import yt_dlp
import os

# MP3 다운로드 함수
def get_mp3_from_youtube(url, mp3_filename_base):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': mp3_filename_base,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'cookiefile': 'cookies.txt'  # 유튜브 로그인 쿠키 사용
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return mp3_filename_base + '.mp3'

# Streamlit UI
st.title("🎵 YouTube MP3 Downloader")

# 사용자 입력 (유튜브 링크)
url = st.text_input("유튜브 링크를 입력하세요:")

if st.button("다운로드 시작"):
    if url:
        st.info("⏳ 다운로드 중... 잠시만 기다려주세요.")

        # 파일 이름 설정
        mp3_filename_base = "downloaded_audio"
        mp3_file = get_mp3_from_youtube(url, mp3_filename_base)

        if os.path.exists(mp3_file):
            st.success("✅ 다운로드 완료! 아래 버튼을 눌러 MP3를 저장하세요.")
            st.audio(mp3_file, format="audio/mp3")  # 오디오 플레이어 추가
            with open(mp3_file, "rb") as f:
                st.download_button(
                    label="📥 MP3 다운로드",
                    data=f,
                    file_name="youtube_audio.mp3",
                    mime="audio/mp3"
                )
        else:
            st.error("❌ 다운로드 실패! 유효한 유튜브 링크인지 확인하세요.")
    else:
        st.warning("⚠️ 유튜브 링크를 입력하세요.")
