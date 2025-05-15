import json
import csv
import argparse
import os
from typing import List, Dict

def parse_arguments():
    """命令行参数解析"""
    parser = argparse.ArgumentParser(description='Convert JSON file to CSV')
    parser.add_argument('input_json', help='Input JSON file path')
    parser.add_argument('output_csv', help='Output CSV file path')
    parser.add_argument('--flatten', action='store_true',
                      help='Flatten nested JSON objects (default: False)')
    parser.add_argument('--delimiter', default=',',
                      help='CSV delimiter character (default: ,)')
    return parser.parse_args()

def read_json_file(file_path: str) -> List[Dict]:
    """读取并验证JSON文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict) and 'list' in data:
            return data['list']
        return data if isinstance(data, list) else [data]
    except Exception as e:
        raise RuntimeError(f"JSON读取失败: {str(e)}")

def flatten_data(data: Dict, parent_key: str = '', sep: str = '.') -> Dict:
    """递归展平嵌套字典"""
    items = {}
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_data(v, new_key, sep))
        else:
            items[new_key] = v
    return items

def write_to_csv(data: List[Dict], output_path: str, config: argparse.Namespace):
    """生成CSV文件"""
    try:
        # 处理字段名和数据展平
        processed_data = [flatten_data(item) if config.flatten else item for item in data]
        fieldnames = sorted({key for item in processed_data for key in item.keys()})

        # 写入文件
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=config.delimiter)
            writer.writeheader()
            writer.writerows(processed_data)
            
    except Exception as e:
        raise RuntimeError(f"CSV生成失败: {str(e)}")

def main():
    """主执行流程"""
    args = parse_arguments()
    
    # 输入文件验证
    if not os.path.exists(args.input_json):
        raise FileNotFoundError(f"输入文件不存在: {args.input_json}")
    
    # 执行转换
    json_data = read_json_file(args.input_json)
    write_to_csv(json_data, args.output_csv, args)
    print(f"成功转换 {len(json_data)} 条记录至 {args.output_csv}")

if __name__ == "__main__":
    main()