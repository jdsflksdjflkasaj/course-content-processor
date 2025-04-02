import os
import yaml
import argparse
import logging
from pathlib import Path
import subprocess
import json
import requests

class CourseProcessor:
    def __init__(self, config_path):
        self.config = self._load_config(config_path)
        self._setup_logging()
        self._setup_directories()
        
    def _load_config(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
            
    def _setup_logging(self):
        logging.basicConfig(
            level=getattr(logging, self.config['logging']['level']),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.config['logging']['file']),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def _setup_directories(self):
        for path in self.config['paths'].values():
            Path(path).mkdir(parents=True, exist_ok=True)
            
    def extract_subtitle(self, video_path):
        """使用 SubtitleEdit 提取字幕"""
        output_path = os.path.join(
            self.config['paths']['output'],
            f"{Path(video_path).stem}_subtitle.txt"
        )
        
        # 调用 SubtitleEdit CLI
        cmd = [
            "SubtitleEdit",
            "/convert",
            video_path,
            output_path,
            "/format:txt"
        ]
        
        try:
            subprocess.run(cmd, check=True)
            self.logger.info(f"字幕提取成功：{output_path}")
            return output_path
        except subprocess.CalledProcessError as e:
            self.logger.error(f"字幕提取失败：{e}")
            raise
            
    def generate_summary(self, subtitle_path):
        """使用 DeepSeek 生成内容总结"""
        with open(subtitle_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 调用 DeepSeek API
        headers = {
            "Authorization": f"Bearer {self.config['ai']['api_key']}",
            "Content-Type": "application/json"
        }
        
        prompt = self._load_template("summary")
        data = {
            "prompt": prompt.format(content=content),
            "max_tokens": self.config['processing']['summary']['max_length']
        }
        
        try:
            response = requests.post(
                "https://api.deepseek.com/v1/completions",
                headers=headers,
                json=data
            )
            response.raise_for_status()
            
            summary = response.json()["choices"][0]["text"]
            output_path = os.path.join(
                self.config['paths']['output'],
                f"{Path(subtitle_path).stem}_summary.md"
            )
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(summary)
                
            self.logger.info(f"内容总结生成成功：{output_path}")
            return output_path
        except Exception as e:
            self.logger.error(f"内容总结生成失败：{e}")
            raise
            
    def create_mindmap(self, summary_path):
        """生成思维导图"""
        with open(summary_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        prompt = self._load_template("mindmap")
        
        # 调用 DeepSeek API 生成思维导图
        headers = {
            "Authorization": f"Bearer {self.config['ai']['api_key']}",
            "Content-Type": "application/json"
        }
        
        data = {
            "prompt": prompt.format(content=content),
            "max_tokens": 2000
        }
        
        try:
            response = requests.post(
                "https://api.deepseek.com/v1/completions",
                headers=headers,
                json=data
            )
            response.raise_for_status()
            
            mindmap = response.json()["choices"][0]["text"]
            output_path = os.path.join(
                self.config['paths']['output'],
                f"{Path(summary_path).stem}_mindmap.md"
            )
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(mindmap)
                
            self.logger.info(f"思维导图生成成功：{output_path}")
            return output_path
        except Exception as e:
            self.logger.error(f"思维导图生成失败：{e}")
            raise
            
    def _load_template(self, template_name):
        """加载模板文件"""
        template_path = self.config['templates'][template_name]
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
            
    def process(self, video_path):
        """处理完整工作流"""
        try:
            self.logger.info(f"开始处理视频：{video_path}")
            
            # 1. 提取字幕
            subtitle_path = self.extract_subtitle(video_path)
            
            # 2. 生成内容总结
            summary_path = self.generate_summary(subtitle_path)
            
            # 3. 创建思维导图
            mindmap_path = self.create_mindmap(summary_path)
            
            self.logger.info("处理完成！")
            return {
                "subtitle": subtitle_path,
                "summary": summary_path,
                "mindmap": mindmap_path
            }
        except Exception as e:
            self.logger.error(f"处理失败：{e}")
            raise

def main():
    parser = argparse.ArgumentParser(description="课程内容处理工具")
    parser.add_argument("video", help="输入视频文件路径")
    parser.add_argument("--config", default="config/config.yaml", help="配置文件路径")
    args = parser.parse_args()
    
    processor = CourseProcessor(args.config)
    results = processor.process(args.video)
    
    print("\n处理结果：")
    print(f"字幕文件：{results['subtitle']}")
    print(f"内容总结：{results['summary']}")
    print(f"思维导图：{results['mindmap']}")

if __name__ == "__main__":
    main()