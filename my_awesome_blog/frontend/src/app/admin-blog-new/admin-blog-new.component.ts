import { Component } from '@angular/core';
import { Doc, NawahService, Res } from 'ng-nawah';

@Component({
	selector: 'app-admin-blog-new',
	templateUrl: './admin-blog-new.component.html',
	styleUrls: ['./admin-blog-new.component.css']
})
export class AdminBlogNewComponent {

	doc: {
		title: {
			ar_AE: string;
			en_AE: string;
		},
		content: {
			ar_AE: string;
			en_AE: string;
		},
	} = {
			title: {
				ar_AE: undefined,
				en_AE: undefined,
			},
			content: {
				ar_AE: undefined,
				en_AE: undefined,
			},
		};

	msg: {
		type?: 'success' | 'fail';
		content?: string;
	} = {};


	constructor(private nawah: NawahService) { }

	createBlogPost(): void {
		this.msg = {};
		this.nawah.call({
			endpoint: 'blog/create',
			doc: this.doc
		}).subscribe({
			next: (res) => {
				this.msg = {
					type: 'success',
					content: res.msg
				};
			},
			error: (res: Res<Doc>) => {
				this.msg = {
					type: 'fail',
					content: res.msg || (res as any)
				};
			}
		});
	}

}
